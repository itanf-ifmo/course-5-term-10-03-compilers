import itertools


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
        self._type = t
        self._position = position

    def resolve(self, context):
        return []

    def exception(self, msg):
        return CompileError(self._context, self._position[0], self._position[1], msg)

    @property
    def type(self):
        return self._type

    def __len__(self):
        return 0


class FunctionStatement(Statement):
    def __init__(self, context, return_type, name, parameters, body, position):
        super().__init__(context, 'void', position)

        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body
        p = '(' + ','.join(t for t, n in parameters) + ')'
        sp = name + p

        self.signature = p + '->' + return_type

        # if sp in context.functions:
        #     raise self.exception('functions with such signature already exists')
        if name in context.variables:
            raise self.exception('function with name {} already defined!'.format(name))

        self.number = len(context.functions)
        context.functions[sp] = self

        self.var = context.variables.new(name, self.signature)
        # self.var = context.variables.new(sp, 'Function<%s>' % self.signature)

        self.seq = ['sipush', format(self.number, '04x')] + self.var.update(context)

    def __len__(self):
        return len(self.seq)

    @property
    def len(self):
        return sum(len(i) for i in self.body)

    def r(self, context):
        context.push('fc', (0, 0))

        for p_type, p_name in self.parameters:
            context.variables.new(p_name, p_type)

        r = list(itertools.chain(*[i.resolve(context) for i in self.body]))

        context.pop((0, 0))
        return r

    def resolve(self, context):
        return self.seq


class FunctionCallStatement(Statement):
    def __init__(self, context, name, parameters, position):
        super().__init__(context, 'void', position)
        t = '(' + ','.join(e.type for e in parameters) + ')'
        self.parameters = parameters
        self.signature = t + '->?'

        if name not in context.variables:
            raise self.exception('unable to find function ' + self.signature)

        self.var = context.variables[name]
        if not self.var.type.startswith(t):
            raise self.exception(
                'Mismatch signatures of called function: expected {} but was {}'.format(self.var.type, self.signature)
            )

        self.return_type = self.var.type[len(t + '->'):]

        self.seq = self.var.resolve(context)
        self.params_len = sum(9 + len(e) for e in parameters)
        self.tail = ['pop']

    def call_from_expression(self):
        self.tail = []
        self._type = self.return_type
        return self

    def __len__(self):
        return self.params_len + len(self.seq) + 3 + len(self.tail)

    def resolve(self, context):
        params = []

        n = context.variables.full_len
        for expr in self.parameters[::-1]:
            params += expr.resolve(context)

        for e in self.parameters:
            params += [
                'getstatic', context.constant_pull['st'], '',
                'swap',
                'sipush', format(n, '04x'), '',
                'swap',
                'iastore',
            ]

            n += 1

        return params + self.seq + [
            'sipush', format(context.variables.full_len, '04x'), '',
            'invokestatic', context.constant_pull['sw:(II)I'], '',
        ] + self.tail


class FunctionExprCallStatement(Statement):
    def __init__(self, context, expr, parameters, position):
        super().__init__(context, 'void', position)
        assert isinstance(expr, Statement)

        t = '(' + ','.join(e.type for e in parameters) + ')'
        self.parameters = parameters
        self.signature = t + '->?'

        if not expr.type.startswith(t):
            raise self.exception(
                'Mismatch signatures of called function: expected {} but was {}'.format(self.var.type, self.signature)
            )

        self.return_type = expr.type[len(t + '->'):]

        self.expr = expr
        self.params_len = sum(9 + len(e) for e in parameters)
        self.tail = ['pop']

    def call_from_expression(self):
        self.tail = []
        self._type = self.return_type
        return self

    def __len__(self):
        return self.params_len + len(self.expr) + 5 + len(self.tail)

    def resolve(self, context):
        params = []

        n = context.variables.full_len
        for expr in self.parameters[::-1]:
            params += expr.resolve(context)

        params2 = []
        for e in self.parameters:
            params2 += [
                'getstatic', context.constant_pull['st'], '',
                'swap',
                'sipush', format(n, '04x'), '',
                'swap',
                'iastore',
            ]

            n += 1

        return params + self.expr.resolve(context) + [
            'istore_2',
        ] + params2 + [
            'iload_2',
            'sipush', format(context.variables.full_len, '04x'), '',
            'invokestatic', context.constant_pull['sw:(II)I'], '',
        ] + self.tail


class BoolStatement(Statement):
    def __init__(self, context, v, position):
        super().__init__(context, 'bool', position)

        self.v = v

    def __len__(self):
        return 1

    def resolve(self, context):
        return [
            'iconst_1' if self.v else 'iconst_0'
        ]

    def __str__(self):
        return 'iconst_1' if self.v else 'iconst_0'


class ReturnStatement(Statement):
    def __init__(self, context, expr, position):
        super().__init__(context, 'void', position)
        assert expr is None or isinstance(expr, Statement)
        self.expr = expr

        actual_return_type = 'void' if self.expr is None else self.expr.type
        expected_return_type = context.variables.function_return_type
        if expected_return_type != actual_return_type:
            raise self.exception('This function should return {} but found {}'.format(
                expected_return_type, actual_return_type
            ))

    def __len__(self):
        return (len(self.expr) if self.expr is not None else 3) + 1

    def resolve(self, context):
        if self.expr:
            return self.expr.resolve(context) + [
                'ireturn'
            ]
        else:
            return [
                'sipush', '00', '00',
                'ireturn'
            ]


class PassStatement(Statement):
    def __init__(self, context, position):
        super().__init__(context, 'void', position)

    def __len__(self):
        return 1

    def resolve(self, context):
        return [
            'nop'
        ]


class PrintStatement(Statement):
    def __init__(self, context, expr, position):
        super().__init__(context, 'void', position)

        assert isinstance(expr, Statement)
        self.expr = expr
        if expr.type == 'void':
            raise self.exception('could not print void')

    def __len__(self):
        return len(self.expr) + 3 + 3

    # noinspection PyTypeChecker
    def resolve(self, context):
        t = context.constant_pull['println:(Z)V'] if self.expr.type == 'bool' else context.constant_pull['println:(I)V']
        return [
            'getstatic',
            context.constant_pull['System.out.PrintStream'], '',
        ] + self.expr.resolve(context) + [
            'invokevirtual',
            t, '',
        ]


class ReadStatement(Statement):
    def __init__(self, context, variable_name, position):
        super().__init__(context, 'void', position)

        if variable_name not in context.variables:
            raise self.exception('Undefined variable {}'.format(context.variables))

        self.var = context.variables[variable_name]

        self.update_seq = self.var.update(context)

        read_seq = [
            'getstatic',
            context.constant_pull['System.in.InputStream'], '',
            'invokevirtual',
            context.constant_pull['read:()I'], ''
        ]

        if self.var.type == 'int':
            self.seq = [
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
        elif self.var.type == 'bool':
            self.seq = read_seq + [
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
            raise self.exception('Could not read variable of type {}'.format(self.var.type))

        self.seq += self.update_seq

    def __len__(self):
        return len(self.seq)

    def resolve(self, context):
        return self.seq


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
        super().__init__(context, 'bool' if op in self.RETURNS_BOOLEAN else left.type, position)
        assert isinstance(left, Statement)
        assert isinstance(right, Statement)

        if left.type != right.type and op not in self.BOOLEAN_OPERATORS:
            raise self.exception("Type of operand mismatches: {} {} {}".format(left.type, op, right.type))

        if left.type == 'bool' and op not in self.RETURNS_BOOLEAN:
            raise self.exception("Unexpected operator for boolean parameters: {}".format(op))

        self.left = left
        self.right = right

        self.op = self.OP_TO_ASM_MAP[op]

    def __len__(self):
        return len(self.left) + len(self.op) + len(self.right)

    # noinspection PyTypeChecker
    def resolve(self, context):
        # return self.op
        return self.left.resolve(context) + \
               self.right.resolve(context) + \
               self.op


class UnaryOperatorStatement(Statement):
    BOOLEAN_UNARY_OPERATORS = {'!', 'not'}
    OP_TO_ASM_MAP = {
        '!': ['iconst_1', 'ixor'],
        'not': ['iconst_1', 'ixor'],
        '-': ['ineg'],
    }

    def __init__(self, context, op, expr, position):
        super().__init__(context, 'bool' if op in self.BOOLEAN_UNARY_OPERATORS else expr.type, position)

        if expr.type == 'bool' and op not in self.BOOLEAN_UNARY_OPERATORS:
            raise self.exception("Unexpected unary operator for boolean expression: {}".format(op))

        assert isinstance(expr, Statement)

        self.expr = expr
        self.op = self.OP_TO_ASM_MAP[op]

    def __len__(self):
        return len(self.expr) + len(self.op)

    def resolve(self, context):
        return self.expr.resolve(context) + \
               self.op


class ConstIntStatement(Statement):
    def __init__(self, context, i, position):
        super().__init__(context, 'int', position)

        self.i = i

    def __len__(self):
        return 3

    def resolve(self, context):
        context.constant_pull['constant_' + str(self.i)] = self.i

        return [
            'ldc_w',
            context.constant_pull['constant_' + str(self.i)], ''
        ]


class DeclareVariableStatement(Statement):
    def __init__(self, context, t, name, position):
        super().__init__(context, 'void', position)
        if name in context.variables.current_scope:
            raise self.exception("Variable {} already defined in this scope".format(name))

        context.variables.new(name, t)
        self.name = name
        self.t = t

    def __len__(self):
        return 0

    def resolve(self, context):
        context.variables.new(self.name, self.t)

        return []


class GetVariableStatement(Statement):
    def __init__(self, context, name, position):
        super().__init__(context, 'void', position)

        if name not in context.variables:
            raise self.exception("Variable {} is not defined".format(name))
        variable = context.variables[name]
        self._type = variable.type

        self.variable = variable
        self.seq = self.variable.resolve(context)

    def __len__(self):
        return len(self.seq)

    def resolve(self, context):
        return self.seq


class AssignVariableStatement(Statement):
    def __init__(self, context, name, expr, position):
        super().__init__(context, 'void', position)
        assert isinstance(expr, Statement)

        if name not in context.variables:
            raise self.exception("Variable {} is not defined".format(name))

        variable = context.variables[name]

        if variable.type != expr.type:
            raise self.exception("Type {} of variable {} doesn't matches expression type {}".format(
                variable.type, name, expr.type))

        self.variable = variable
        self.expr = expr
        self.seq = self.variable.update(context)

    def __len__(self):
        return len(self.expr) + len(self.seq)

    def resolve(self, context):
        return self.expr.resolve(context) + \
               self.seq


class DeclareAndAssignVariableStatement(Statement):
    def __init__(self, context, t, name, expr, position):
        super().__init__(context, 'void', position)
        assert isinstance(expr, Statement)

        if name in context.variables.current_scope:
            raise self.exception("Variable {} already defined in this scope".format(name))

        variable = context.variables.new(name, t)

        if variable.type != expr.type:
            raise self.exception("Type {} of variable {} doesn't matches expression type {}".format(
                variable.type, name, expr.type))

        self.variable = variable
        self.expr = expr
        self.seq = self.variable.update(context)
        self.name = name
        self.t = t

    def __len__(self):
        return len(self.expr) + len(self.seq)

    def resolve(self, context):
        context.variables.new(self.name, self.t)

        return self.expr.resolve(context) + self.seq


class IfStatement(Statement):
    def __init__(self, context, expr, true_seq, false_seq, position):
        super().__init__(context, 'void', position)
        assert isinstance(expr, Statement)
        assert isinstance(true_seq, Statement)
        assert false_seq is None or isinstance(false_seq, Statement)

        self.expr = expr
        self.ts, self.fs = len(true_seq), (len(false_seq) if false_seq is not None else 0)
        self.true_seq = true_seq
        self.false_seq = false_seq

    def __len__(self):
        return len(self.expr) + 3 + self.fs + 3 + self.ts

    def resolve(self, context):
        return self.expr.resolve(context) + [
            'ifne',
            format(3 + self.fs + 3, '04x'), '',
        ] + (self.false_seq.resolve(context) if self.false_seq is not None else []) + [
           'goto',
           format(3 + self.ts, '04x'), '',
        ] + self.true_seq.resolve(context)


class WhileStatement(Statement):
    def __init__(self, context, expr, seq, position):
        super().__init__(context, 'void', position)
        assert isinstance(expr, Statement)
        assert isinstance(seq, Statement)

        self.expr = expr
        self.seq = seq
        self.seq_size = len(seq)
        self.expr_size = len(expr)

    def __len__(self):
        return len(self.expr) + 3 + self.seq_size + 3

    def resolve(self, context):
        return self.expr.resolve(context) + [
            'ifeq',
            format(3 + self.seq_size + 3, '04x'), '',
        ] + self.seq.resolve(context) + [
           'goto', '',
           format(256 * 256 - 3 - self.seq_size - self.expr_size, '04x'),
        ]


class ScopeStatement(Statement):
    def __init__(self, context, body, position):
        super().__init__(context, 'void', position)
        self.body = body

    def __len__(self):
        return sum(len(i) for i in self.body)

    def resolve(self, context):
        context.push('s', (0, 0))
        r = list(itertools.chain(*[i.resolve(context) for i in self.body]))
        context.pop((0, 0))
        return r


class Variable:
    def __init__(self, cl, t, name, number):
        self.type = t
        self.name = name
        self.number = format(number, '04x')
        self.closure = cl

    def update(self, context):
        if self.is_global:
            # print('g', self, self.number)

            return [
                'getstatic', context.constant_pull['st'], '',
                'swap',
                'sipush', self.number, '',
                'swap',
                'iastore',
            ]

        # print('l', self, self.number)
        return [
            'getstatic', context.constant_pull['st'], '',
            'swap',
            'sipush', self.number, '', 'iload_1', 'iadd',
            'swap',
            'iastore',
        ]

    def resolve(self, context):
        if self.is_global:
            # print('g', self, self.number)

            return [
                'getstatic', context.constant_pull['st'], '',
                'sipush', self.number, '',
                'iaload',
            ]

        # print('l', self, self.number)
        return [
            'getstatic', context.constant_pull['st'], '',
            'sipush', self.number, '', 'iload_1', 'iadd',
            'iaload',
        ]

    @property
    def is_global(self):
        return self.closure.is_global

    def __str__(self):
        return "({}) {} : {}".format(self.number, self.type, self.name)


class Variables:
    def __init__(self, context, previous, s, function_return_type):
        # todo count locals
        self._previous = previous
        self._current = {}
        self._context = context
        self._s = s
        self._function_return_type = function_return_type

    @property
    def current_scope(self):
        return self._current

    def new(self, name, t):
        self._current[name] = Variable(self, t, name, len(self))
        return self._current[name]

    @property
    def is_global(self):
        return self._previous is None

    @property
    def number_of_non_global_vars(self):
        return 0 if self.is_global else (len(self._current) + self._previous.number_of_non_global_vars)

    @property
    def previous(self):
        return self._previous

    @property
    def full_len(self):
        return (0 if self._previous is None else self._previous.full_len) + len(self._current)

    @property
    def function_return_type(self):
        if self._function_return_type is not None:
            return self._function_return_type

        if self._previous is None:
            return None

        return self._previous.function_return_type

    def __len__(self):
        if self._s == 'f':
            return len(self._current)

        return (0 if self._previous is None else len(self._previous)) + len(self._current)

    def __contains__(self, item):
        if item in self._current:
            return True

        if self._previous is None:
            return False

        return self._previous[item]

    def __getitem__(self, item):
        if item in self._current:
            return self._current[item]

        if self._previous is None:
            return None

        return self._previous[item]

    def __str__(self):
        return '------ ' + self._s + ' ------\n' + '\n'.join(str(x) for x in self._current.values()) +\
               ('\n' + str(self._previous) if self._previous is not None else '') + '\n============\n'


class Context:
    def __init__(self, source, cp):
        self.file = None
        self.source = source
        self.constant_pull = cp
        self.variables = Variables(self, None, 'g', None)
        self.functions = dict()
        self.get_stream_size = 32

    def push(self, t, _, function_return_type=None):
        self.variables = Variables(self, self.variables, t, function_return_type)

    def pop(self, p):
        self.variables = self.variables.previous

        if self.variables is None:
            raise CompileError(self, p[0], p[1], 'Unexpectedly empty context')

    def build_functions_table(self):
        number_of_functions = len(self.functions)
        full_bodies_length = sum(f.len + 3 for f in self.functions.values())

        switch_size = 9 + number_of_functions * 8 + full_bodies_length + 2

        table = ''
        tmp_size = 0
        for n, f in sorted((f.number, f) for f in self.functions.values()):
            table += format(n, '08x')
            table += format(9 + 8 * number_of_functions + tmp_size, '08x')
            tmp_size += f.len + 3

        bodies = []
        tmp_size = full_bodies_length
        for n, f in sorted((f.number, f) for f in self.functions.values()):
            tmp_size -= f.len + 3
            bodies += f.r(self)
            bodies += ['goto', format(tmp_size + 3, '04x')]

        return [
            'nop', 'nop', 'nop', 'nop', 'nop', 'nop', 'iload_0',
            'lookupswitch',
            format(switch_size - 2, '08x'),      # def
            format(number_of_functions, '08x'),  # num of functions
            table,
        ] + bodies + [
            'sipush', '0000',
            'ireturn',
        ]

    def push_func_params(self, params):

        for p_type, p_name in params:
            self.variables.new(p_name, p_type)
