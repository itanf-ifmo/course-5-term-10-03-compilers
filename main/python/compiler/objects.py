import itertools
import random
import uuid


class CompilerError(BaseException):
    def __init__(self, context, line, column, message):
        p = 'Error: {} at ({}, {}):\n'.format(message, line, column)

        p += '\n'.join(context.source.split('\n')[max(0, line - 2):][:2])
        p += '\n' + (' ' * column) + '^'

        if context.file:
            p += '\n File "{}", line {}'.format(context.file, line)

        super().__init__(p)


class CompileError(CompilerError):
    pass


class ParseError(CompilerError):
    pass


class Statement:
    def __init__(self, context, t, position):
        self._context = context
        assert isinstance(context.variables, Variables)
        self._vars = context.variables
        self._type = t
        self._position = position

    def resolve(self):
        return []

    def optimize(self):
        raise self.exception('not optimize')

    @property
    def seq(self):
        return self.resolve()

    def exception(self, msg):
        return CompileError(self._context, self._position[0], self._position[1], msg)

    def typecheck(self):
        raise self.exception('not checked')

    @property
    def vars(self):
        return self._vars

    @property
    def ctx(self):
        assert isinstance(self._context, Context)
        return self._context

    @property
    def type(self):
        return self._type

    def __len__(self):
        return 0


class SpecialStatement(Statement):
    def __init__(self, context, _vars, seq):
        super().__init__(context, 'undefined', (0, 0))
        self._vars = _vars
        self._seq = seq

    def __len__(self):
        return len(self._seq)

    def typecheck(self):
        self._type = 'void'

    def optimize(self):
        pass

    def resolve(self):
        return self._seq


class FunctionStatement(Statement):
    def __init__(self, context, return_type, name, parameters, position):
        context.push('f', return_type)

        super().__init__(context, 'undefined', position)

        if name is None:
            name = 'lambda<%d>' % random.randint(10 ** 5, 10 ** 6)
            self.lambda_f = True
        else:
            self.lambda_f = False

        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = None
        self.signature = '(' + ','.join(t for t, n in parameters) + ')' + '->' + return_type
        self.number = len(context.functions)
        context.functions[self.name + self.signature] = self

        self._seq = [
            'iconst_2',
            'anewarray', self.ctx.constant_pull['Object class'], '',
            'dup',
            'iconst_0',
            'sipush', format(self.number, '04x'), '',
            'invokestatic', self.ctx.constant_pull['box'], '',
            'aastore',
            'dup',
            'iconst_1',
            'aload_0',
            'aastore',
        ]

        if not self.lambda_f:
            if name in self.vars.previous.current_scope:
                raise self.exception('function(or variable) with name {} already defined!'.format(name))

            variable = self.vars.previous.new(name, self.signature)
            variable.function = self

            self._seq += variable.update()

        for p_type, p_name in parameters:
            self.vars.new(p_name, p_type)

        self.ctx.max_arguments = max(self.ctx.max_arguments, len(self.parameters))

    def build(self, body):
        self.body = body

        if self.return_type != 'void' and self.body and isinstance(self.body[-1], ExpressionStatement):
            # noinspection PyUnresolvedReferences
            self.body[-1].used()

        if self.body:
            self.body = [self._load_arguments()] + self.body

        self.ctx.pop()

    def _load_arguments(self):
        params = []
        for n in range(len(self.parameters)):
            tsa = [
                'checkcast', self.ctx.constant_pull['java/lang/Integer class'], '',
                'invokevirtual', self.ctx.constant_pull['unbox'], '',
            ]

            if '->' in self.parameters[n][0]:
                tsa = []

            params += [
                'getstatic', self.ctx.constant_pull['args_st'], '',
                'sipush', format(n, '04x'), '',
                'aaload',
            ] + tsa + self.vars[self.parameters[n][1]].update()

        s = SpecialStatement(self.ctx, self.vars, params)

        return s

    def optimize(self):
        if not self.body:
            return

        i = self.body[-1]

        # noinspection PyUnresolvedReferences
        if (isinstance(i, ReturnStatement) or isinstance(i, ExpressionStatement)) and \
                isinstance(i.expr, FunctionExprCallStatement) and \
                isinstance(i.expr.expr, GetVariableStatement) and \
                i.expr.expr.variable.function and \
                i.expr.expr.variable.function is self:

            params_build = sum([param.seq for param in i.expr.parameters[::-1]], [])

            create_new_scope = [
                'sipush', format(len(self.vars), '04x'), '',
                'anewarray', self.ctx.constant_pull['Object class'], '',
                'dup',
                'iconst_0',
                'aload_0',
                'iconst_0',
                'aaload',
                'aastore',
                'astore_0',
            ]

            params_store = sum([self.vars[param_name].update() for param_type, param_name in self.parameters], [])

            label_uuid = str(uuid.uuid1())

            self.body = [
                self.body[0],
                SpecialStatement(self.ctx, self.vars, [
                    ':TRO-%s' % label_uuid
                ])
            ] + self.body[1:][:-1] + [
                SpecialStatement(self.ctx, self.vars, params_build + create_new_scope + params_store + [
                    'goto', '#TRO-%s' % label_uuid, '',
                ])
            ]

    def __len__(self):
        return len(self._seq)

    @property
    def len(self):
        return 11 + sum(len(i) for i in self.body)

    def typecheck(self):
        for i in self.body:
            i.typecheck()

        self._type = self.signature if self.lambda_f else 'void'

    def r(self):
        return [
            'sipush', format(len(self.vars), '04x'), '',
            'anewarray', self.ctx.constant_pull['Object class'], '',
            'dup',
            'iconst_0',
            'aload_0',
            'aastore',
            'astore_0',
        ] + list(itertools.chain(*[i.seq for i in self.body]))

    def resolve(self):
        return self._seq


class FunctionExprCallStatement(Statement):
    def __init__(self, context, expr, parameters, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(expr, Statement)

        self.parameters = parameters

        self.expr = expr
        self.signature = None

        self.return_type = None
        self.tail = ['pop']

    def call_from_expression(self):
        self.tail = []
        return self

    def __len__(self):
        return len(self.expr) + sum(len(e) + 9 + 1 for e in self.parameters) + 3 + len(self.tail)

    def typecheck(self):
        self.expr.typecheck()

        for p in self.parameters:
            p.typecheck()

        t = '(' + ','.join(e.type for e in self.parameters) + ')'
        self.signature = t + '->?'

        if not self.expr.type.startswith(t):
            raise self.exception(
                'Mismatch signatures of called function: expected {} but was {}'.format(self.expr.type, self.signature)
            )

        self.return_type = self.expr.type[len(t + '->'):]
        self._type = 'void' if self.tail else self.return_type

        tsa = [
            'checkcast', self.ctx.constant_pull['java/lang/Integer class'], '',
            'invokevirtual', self.ctx.constant_pull['unbox'], '',
        ]

        if '->' in self.return_type:
            tsa = []

        self.tail += tsa

    def optimize(self):
        for p in self.parameters:
            p.optimize()

    def resolve(self):
        params = []

        for n, param in enumerate(self.parameters):
            tsa = [
                'invokestatic', self.ctx.constant_pull['box'], '',
            ]

            if '->' in param.type:
                tsa = [
                    'nop', 'nop', 'nop',
                ]

            params += [
                'getstatic', self.ctx.constant_pull['args_st'], '',
                'sipush', format(n, '04x'), '',
            ] + param.seq + tsa

        params += [
           'aastore',
        ] * len(self.parameters)

        return self.expr.seq + params + [
            'invokestatic', self.ctx.constant_pull['call'], '',
        ] + self.tail


class ExpressionStatement(Statement):
    def __init__(self, context, expr, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(expr, Statement)
        self.expr = expr
        self._used = False
        self.tail = ['pop']

    def __len__(self):
        return len(self.expr) + len(self.tail)

    def used(self):
        assert self.type == 'undefined'
        self._used = True

    def typecheck(self):
        self.expr.typecheck()
        self._type = 'void' if self._used else self.expr.type

        if self._used:
            if '->' not in self.expr.type:
                self.tail = [
                    'invokestatic', self.ctx.constant_pull['box'], '',
                    'areturn'
                ]
            else:
                self.tail = ['areturn']

    def optimize(self):
        self.expr.optimize()

    def resolve(self):
        return self.expr.seq + self.tail


class BoolStatement(Statement):
    def __init__(self, context, v, position):
        super().__init__(context, 'undefined', position)

        self.v = v

    def __len__(self):
        return 1

    def typecheck(self):
        self._type = 'bool'

    def optimize(self):
        pass

    def resolve(self):
        return [
            'iconst_1' if self.v else 'iconst_0'
        ]


class ReturnStatement(Statement):
    def __init__(self, context, expr, position):
        super().__init__(context, 'undefined', position)
        assert expr is None or isinstance(expr, Statement)
        self.expr = expr
        self.expected_return_type = self.vars.function_return_type
        self._seq = None

    def __len__(self):
        return len(self._seq)

    def typecheck(self):
        if self.expr is not None:
            self.expr.typecheck()

        actual_return_type = 'void' if self.expr is None else self.expr.type

        if self.expected_return_type != actual_return_type:
            raise self.exception('This function should return {} but found {}'.format(
                self.expected_return_type, actual_return_type
            ))

        self._type = 'void'

        if self.expr:
            tsa = [
                'invokestatic', self.ctx.constant_pull['box'], '',
            ]

            if '->' in self.expr.type:
                tsa = []

            self._seq = self.expr.seq + tsa + [
                'areturn'
            ]
        else:
            self._seq = [
                'iconst_0',
                'invokestatic', self.ctx.constant_pull['box'], '',
                'areturn'
            ]

    def optimize(self):
        if self.expr is not None:
            self.expr.optimize()

    def resolve(self):
        return self._seq


class PassStatement(Statement):
    def __init__(self, context, position):
        super().__init__(context, 'undefined', position)

    def __len__(self):
        return 1

    def typecheck(self):
        self._type = 'void'

    def optimize(self):
        pass

    def resolve(self):
        return [
            'nop'
        ]


class PrintStatement(Statement):
    def __init__(self, context, expr, position):
        super().__init__(context, 'undefined', position)

        assert isinstance(expr, Statement)
        self.expr = expr

    def __len__(self):
        return len(self.expr) + 3 + 3

    def typecheck(self):
        self.expr.typecheck()
        if self.expr.type == 'void':
            raise self.exception('could not print void')

        self._type = 'void'

    def optimize(self):
        self.expr.optimize()

    def resolve(self):
        return [
            'getstatic',
            self.ctx.constant_pull['System.out.PrintStream'], '',
        ] + self.expr.seq + [
            'invokevirtual',
            self.ctx.constant_pull['printBool' if self.expr.type == 'bool' else 'printInt'], '',
        ]


class ReadStatement(Statement):
    def __init__(self, context, name, position):
        super().__init__(context, 'undefined', position)
        self.name = name
        self._seq = None
        self.variable = None
        self.update_seq = None

    def __len__(self):
        return len(self._seq) + len(self.update_seq)

    def typecheck(self):
        if self.name not in self.vars:
            raise self.exception("Variable(or function) {} is not defined".format(self.name))

        self.variable = self.vars[self.name]
        self.update_seq = self.variable.update()

        read_seq = [
            'getstatic',
            self.ctx.constant_pull['System.in.InputStream'], '',
            'invokevirtual',
            self.ctx.constant_pull['readInt'], ''
        ]

        if self.variable.type == 'int':
            self._seq = [
               'bipush', '01',
               'istore_3',
               'bipush', '00',
               'bipush', '00',
               'pop',
            ] + read_seq + [
               'dup',
               'bipush', format(45, '02x'),
               'if_icmpne', format(6, '04x'), '',
               'bipush', 'ff',
               'istore_3',
               'dup',
               'bipush', format(48, '02x'),
               'if_icmplt', format(256 * 256 - (2 + 1) - (6 + 1) - 9, '04x'), '',
               'dup',
               'bipush', format(57, '02x'),
               'if_icmpgt', format(256 * 256 - (2 + 1) - (6 + 1) - 6 - 9, '04x'), '',
               'bipush', format(48, '02x'),
               'isub',
               'iadd',
               'bipush', format(10, '02x'),
               'imul',
            ] + read_seq + [
               'dup',
               'bipush', format(48, '02x'),
               'if_icmplt', format(12, '04x'), '',
               'dup',
               'bipush', format(57, '02x'),
               'if_icmpgt', format(6, '04x'), '',
               'goto', format(256 * 256 - 25, '04x'), '',
               'pop',
               'bipush', format(10, '02x'),
               'idiv',
               'iload_3',
               'imul',
            ]
        elif self.variable.type == 'bool':
            self._seq = read_seq + [
                'dup',
                'bipush', format(116, '02x'),
                'if_icmpne', format(9, '04x'), '',
                'pop',
                'bipush', '01',
                'goto', format(3 + 2 + 3 + 2, '04x'), '',
                'bipush', format(102, '02x'),
                'if_icmpne', format(256 * 256 - 2 - 3 - 2 - 1 - 3 - 2 - 1 - 6, '04x'), '',
                'bipush', '00',
                'nop',
            ]
        else:
            raise self.exception('Could not read variable of type {}'.format(self.variable.type))

        self._type = 'void'

    def optimize(self):
        pass

    def resolve(self):
        return self._seq + self.update_seq


class OperatorStatement(Statement):
    BOOLEAN_OPERATORS = {'==', '!=', '&&', 'and', '||', 'or'}
    RETURNS_BOOLEAN = {'==', '!=', '&&', 'and', '||', 'or', '<', '<=', '>', '>='}
    OP_TO_ASM_MAP = {
        '*': ['imul'],
        '/': ['idiv'],
        '%': ['irem'],
        '+': ['iadd'],
        '-': ['isub'],

        '<':  ['if_icmplt', '00', '07', 'iconst_0', 'goto', '00', '04', 'iconst_1'],
        '<=': ['if_icmple', '00', '07', 'iconst_0', 'goto', '00', '04', 'iconst_1'],
        '>':  ['if_icmpgt', '00', '07', 'iconst_0', 'goto', '00', '04', 'iconst_1'],
        '>=': ['if_icmpge', '00', '07', 'iconst_0', 'goto', '00', '04', 'iconst_1'],
        '==': ['if_icmpeq', '00', '07', 'iconst_0', 'goto', '00', '04', 'iconst_1'],
        '!=': ['if_icmpne', '00', '07', 'iconst_0', 'goto', '00', '04', 'iconst_1'],

        '&&': ['iand'],
        'and': ['iand'],
        '||': ['ior'],
        'or': ['ior'],
    }

    def __init__(self, context, left, op, right, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(left, Statement)
        assert isinstance(right, Statement)

        self.left = left
        self.right = right

        self.op = op
        self.op_seq = self.OP_TO_ASM_MAP[op]

    def __len__(self):
        return len(self.left) + len(self.op_seq) + len(self.right)

    def typecheck(self):
        self.left.typecheck()
        self.right.typecheck()

        self._type = 'bool' if self.op in self.RETURNS_BOOLEAN else self.left.type

        if self.left.type != self.right.type and self.op not in self.BOOLEAN_OPERATORS:
            raise self.exception("Type of operand mismatches: {} {} {}".format(
                self.left.type,
                self.op,
                self.right.type
            ))

        if self.left.type == 'bool' and self.op not in self.RETURNS_BOOLEAN:
            raise self.exception("Unexpected operator for boolean parameters: {}".format(self.op))

    def optimize(self):
        self.left.optimize()
        self.right.optimize()

    def resolve(self):
        return self.left.seq + \
               self.right.seq + \
               self.op_seq


class UnaryOperatorStatement(Statement):
    BOOLEAN_UNARY_OPERATORS = {'!', 'not'}
    OP_TO_ASM_MAP = {
        '!': ['iconst_1', 'ixor'],
        'not': ['iconst_1', 'ixor'],
        '-': ['ineg'],
    }

    def __init__(self, context, op, expr, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(expr, Statement)

        self.expr = expr
        self.op = op
        self.op_seq = self.OP_TO_ASM_MAP[op]

    def __len__(self):
        return len(self.expr) + len(self.op_seq)

    def typecheck(self):
        self.expr.typecheck()

        self._type = 'bool' if self.op in self.BOOLEAN_UNARY_OPERATORS else self.expr.type

        if self.expr.type == 'bool' and self.op not in self.BOOLEAN_UNARY_OPERATORS:
            raise self.exception("Unexpected unary operator for boolean expression: {}".format(self.op))

    def optimize(self):
        self.expr.optimize()

    def resolve(self):
        return self.expr.seq + \
               self.op_seq


class ConstIntStatement(Statement):
    def __init__(self, context, i, position):
        super().__init__(context, 'undefined', position)

        self.i = i

    def typecheck(self):
        self._type = 'int'

    def __len__(self):
        return 3

    def optimize(self):
        pass

    def resolve(self):
        self.ctx.constant_pull['constant_' + str(self.i)] = self.i

        return [
            'ldc_w',
            self.ctx.constant_pull['constant_' + str(self.i)], ''
        ]


class DeclareVariableStatement(Statement):
    def __init__(self, context, t, name, position):
        super().__init__(context, 'undefined', position)

        if name in self.vars.current_scope:
            raise self.exception("Variable {} already defined in this scope".format(name))

        self.variable = self.vars.new(name, t)
        self.name = name
        self.t = t

    def __len__(self):
        return 0

    def typecheck(self):
        self._type = 'void'

    def optimize(self):
        pass

    def resolve(self):
        return []


class GetVariableStatement(Statement):
    def __init__(self, context, name, position):
        super().__init__(context, 'undefined', position)
        self.name = name
        self.variable = None
        self._seq = None

    def __len__(self):
        return len(self._seq)

    def typecheck(self):
        if self.name not in self.vars:
            raise self.exception("Variable(or function) {} is not defined".format(self.name))

        self.variable = self.vars[self.name]

        self._type = self.variable.type
        self._seq = self.variable.seq

    def optimize(self):
        pass

    def resolve(self):
        return self._seq


class AssignVariableStatement(Statement):
    def __init__(self, context, name, expr, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(expr, Statement)
        self.name = name
        self.expr = expr
        self.variable = None
        self._seq = None

    def __len__(self):
        return len(self.expr) + len(self._seq)

    def typecheck(self):
        self.expr.typecheck()

        if self.name not in self.vars:
            raise self.exception("Variable {} is not defined".format(self.name))

        self.variable = self.vars[self.name]

        if self.variable.type != self.expr.type:
            raise self.exception("Type {} of variable {} doesn't matches expression type {}".format(
                self.variable.type, self.name, self.expr.type))

        self._seq = self.variable.update()
        self._type = 'void'

    def optimize(self):
        self.expr.optimize()

    def resolve(self):
        return self.expr.seq + \
               self._seq


class DeclareAndAssignVariableStatement(Statement):
    def __init__(self, context, t, name, expr, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(expr, Statement)

        if name in self.vars.current_scope:
            raise self.exception("Variable {} already defined in this scope".format(name))

        self.variable = self.vars.new(name, t)
        self.expr = expr
        self._seq = self.variable.update()
        self.name = name
        self.t = t

    def __len__(self):
        return len(self.expr) + len(self._seq)

    def typecheck(self):
        self.expr.typecheck()

        if self.variable.type != self.expr.type:
            raise self.exception("Type {} of variable {} doesn't matches expression type {}".format(
                self.variable.type, self.name, self.expr.type))

        self._type = 'void'

    def optimize(self):
        self.expr.optimize()

    def resolve(self):
        return self.expr.seq + \
               self._seq


class IfStatement(Statement):
    def __init__(self, context, expr, true_seq, false_seq, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(expr, Statement)
        assert isinstance(true_seq, Statement)
        assert false_seq is None or isinstance(false_seq, Statement)

        self.expr = expr
        self.ts, self.fs = None, None
        self.true_seq = true_seq
        self.false_seq = false_seq

    def __len__(self):
        return len(self.expr) + 3 + self.fs + 3 + self.ts

    def typecheck(self):
        self.expr.typecheck()
        self.true_seq.typecheck()
        if self.false_seq is not None:
            self.false_seq.typecheck()

        self._type = 'void'
        self.ts, self.fs = len(self.true_seq), (len(self.false_seq) if self.false_seq is not None else 0)

    def optimize(self):
        self.expr.optimize()
        self.true_seq.optimize()

        if self.false_seq is not None:
            self.false_seq.optimize()

    def resolve(self):
        return self.expr.seq + [
            'ifne',
            format(3 + self.fs + 3, '04x'), '',
        ] + (self.false_seq.seq if self.false_seq is not None else []) + [
           'goto',
           format(3 + self.ts, '04x'), '',
        ] + self.true_seq.seq


class WhileStatement(Statement):
    def __init__(self, context, expr, seq, position):
        super().__init__(context, 'undefined', position)
        assert isinstance(expr, Statement)
        assert isinstance(seq, Statement)

        self.expr = expr
        self._seq = seq
        self.seq_size = None
        self.expr_size = None

    def __len__(self):
        return len(self.expr) + 3 + self.seq_size + 3

    def typecheck(self):
        self.expr.typecheck()
        self._seq.typecheck()
        self.seq_size = len(self._seq)
        self.expr_size = len(self.expr)
        self._type = 'void'

    def optimize(self):
        self.expr.optimize()
        self._seq.optimize()

    def resolve(self):
        return self.expr.seq + [
            'ifeq',
            format(3 + self.seq_size + 3, '04x'), '',
        ] + self._seq.seq + [
           'goto', '',
           format(256 * 256 - 3 - self.seq_size - self.expr_size, '04x'),
        ]


class ScopeStatement(Statement):
    def __init__(self, context, position):
        context.push('s')
        super().__init__(context, 'undefined', position)

        self.body = None

    def build(self, body):
        self.body = body
        self.ctx.pop()

    def __len__(self):
        return 11 + sum(len(i) for i in self.body) + 7

    def typecheck(self):
        for i in self.body:
            i.typecheck()

        self._type = 'void'

    def optimize(self):
        for b in self.body:
            b.optimize()

    def resolve(self):
        return [
            'sipush', format(len(self.vars), '04x'), '',
            'anewarray', self.ctx.constant_pull['Object class'], '',
            'dup',

            'iconst_0',
            'aload_0',
            'aastore',
            'astore_0',
        ] + list(itertools.chain(*[i.seq for i in self.body])) + [
            'aload_0',
            'iconst_0',
            'aaload',
            'checkcast', self.ctx.constant_pull['[Ljava/lang/Object; class'], '',
            'astore_0',
        ]


class Variable:
    def __init__(self, cl, t, name, number, ctx):
        self.function = '->' in t
        self.type = t
        self.name = name
        self.number = format(number, '04x')
        self.closure = cl
        self.ctx = ctx
        self.depth = None

    def start(self):
        self.depth = 0
        return self

    def pop(self):
        self.depth += 1
        return self

    @property
    def build_context(self):
        return [
            'aload_0'
        ] + [
            'iconst_0',
            'aaload',
            'checkcast', self.ctx.constant_pull['[Ljava/lang/Object; class'], '',
        ] * self.depth

    def update(self):
        ctx = self.build_context

        tsa = [
            'invokestatic', self.ctx.constant_pull['box'], '',
        ]

        if self.function:
            tsa = []

        return ctx + [
            'swap',
            'sipush', self.number, '',
            'swap',
        ] + tsa + [
            'aastore',
        ]

    def resolve(self):
        ctx = self.build_context

        tsa = [
            'checkcast', self.ctx.constant_pull['java/lang/Integer class'], '',
            'invokevirtual', self.ctx.constant_pull['unbox'], '',
        ]

        if self.function:
            tsa = []

        return ctx + [
            'sipush', self.number, '',
            'aaload',
        ] + tsa

    @property
    def seq(self):
        return self.resolve()


class Variables:
    def __init__(self, context, previous, s, function_return_type):
        self._previous = previous
        self._current = {
            None: None
        }
        self._context = context
        self._s = s
        self._function_return_type = function_return_type

    @property
    def current_scope(self):
        return self._current

    def new(self, name, t):
        self._current[name] = Variable(self, t, name, len(self), self._context)
        return self[name]

    @property
    def previous(self):
        return self._previous

    @property
    def function_return_type(self):
        if self._function_return_type is not None:
            return self._function_return_type

        if self._previous is None:
            return None

        return self._previous.function_return_type

    def __len__(self):
        return len(self._current)

    def __contains__(self, item):
        if item in self._current:
            return True

        if self._previous is None:
            return False

        return self._previous[item]

    def __getitem__(self, item):
        if item in self._current:
            return self._current[item].start()

        if self._previous is None:
            return None

        return self._previous[item].pop()


class Context:
    def __init__(self, name, source):
        self.name = name
        self.file = None
        self.source = source
        self.constant_pull = self._generate_constant_pull()
        self.variables = Variables(self, None, 'g', None)
        self.functions = dict()
        self.max_arguments = 0

    def _generate_constant_pull(self):
        from compiler import ConstantPull

        cp = ConstantPull()
        cp['code section'] = 'Code'
        cp['StackMapTable section'] = 'StackMapTable'
        cp['this class name'] = self.name
        cp['Object class name'] = 'java/lang/Object'
        cp.putClass('this class', 'this class name')
        cp.putClass('Object class', 'Object class name')

        cp['main method name'] = 'main'
        cp['main method type'] = '([Ljava/lang/String;)V'

        cp['System class name'] = 'java/lang/System'
        cp.putClass('System', 'System class name')

        cp['in'] = 'in'
        cp['LInputStream'] = 'Ljava/io/InputStream;'
        cp.putNameAndType('in:LInputStream', 'in', 'LInputStream')
        cp.putFieldref('System.in.InputStream', 'System', 'in:LInputStream')

        cp['out'] = 'out'
        cp['LPrintStream'] = 'Ljava/io/PrintStream;'
        cp.putNameAndType('out:LPrintStream', 'out', 'LPrintStream')
        cp.putFieldref('System.out.PrintStream', 'System', 'out:LPrintStream')

        cp['String: stack'] = 'stack'
        cp['String: args_stack'] = 'args_stack'

        cp['[Ljava/lang/Object;'] = '[Ljava/lang/Object;'
        cp['Ljava/lang/Object;'] = 'Ljava/lang/Object;'

        cp.putClass('[Ljava/lang/Object; class', '[Ljava/lang/Object;')
        cp.putClass('Ljava/lang/Object; class', 'Ljava/lang/Object;')

        cp['<clinit>'] = '<clinit>'
        cp['()V'] = '()V'

        cp.putNameAndType('stack:[Ljava/lang/Object;', 'String: stack', '[Ljava/lang/Object;')
        cp.putFieldref('st', 'this class', 'stack:[Ljava/lang/Object;')

        cp.putNameAndType('args_stack:[Ljava/lang/Object;', 'String: args_stack', '[Ljava/lang/Object;')
        cp.putFieldref('args_st', 'this class', 'args_stack:[Ljava/lang/Object;')

        cp.createMethodRef('call', 'A.sw:(Ljava/lang/Object;)Ljava/lang/Object;')

        cp.createMethodRef('readInt', 'java/io/InputStream.read:()I')

        cp.createMethodRef('printInt', 'java/io/PrintStream.println:(I)V')
        cp.createMethodRef('printBool', 'java/io/PrintStream.println:(Z)V')

        cp.createMethodRef('box', 'java/lang/Integer.valueOf:(I)Ljava/lang/Integer;')
        cp.createMethodRef('unbox', 'java/lang/Integer.intValue:()I')

        return cp

    def push(self, t, function_return_type=None):
        self.variables = Variables(self, self.variables, t, function_return_type)

    def pop(self):
        self.variables = self.variables.previous

    def build_functions_table(self):
        number_of_functions = len(self.functions)
        full_bodies_length = sum(f.len + 5 for f in self.functions.values())

        switch_size = 1 + 8 + number_of_functions * (4 + 4) + full_bodies_length

        table = ''
        tmp_size = 1 + 8
        for n, f in sorted((f.number, f) for f in self.functions.values()):
            table += format(n, '08x')
            table += format(number_of_functions * (4 + 4) + tmp_size, '08x')
            tmp_size += f.len + 5

        bodies = []
        tmp_size = full_bodies_length
        for n, f in sorted((f.number, f) for f in self.functions.values()):
            tmp_size -= f.len + 5
            bodies += f.r()
            bodies += [
                'iconst_0',
                'invokestatic', self.constant_pull['box'], '',
                'areturn',
            ]

        return [] + [
            'aload_0',

            'checkcast', self.constant_pull['[Ljava/lang/Object; class'], '',
            'dup',
            'iconst_0',
            'aaload',
            'checkcast', self.constant_pull['java/lang/Integer class'], '',
            'invokevirtual', self.constant_pull['unbox'], '',
            'swap',
            'iconst_1',
            'aaload',
            'astore_0',

            'nop', 'nop', 'nop', 'nop', 'nop', 'nop',

            'lookupswitch',
            format(switch_size, '08x'),          # def
            format(number_of_functions, '08x'),  # num of functions
            table,
        ] + bodies + [
            'aconst_null',
            'areturn',
        ]
