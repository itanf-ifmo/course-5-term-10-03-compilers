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
        context.functions[0] = self
        self.signature = name + '(' + ','.join(t for t, n in parameters) + '):' + return_type


        # print(return_type, name, parameters, body[0])
        # self.body_size = len(body[0])

        # if return_type == 'void':
        #     self.tail = []
        # else:
        #     self.tail = []
        self.var = context.variables.new(self, 'Function<%s>' % self.signature)
        self.number_of_used_vars = 0

        self.used_vars = [

        ]

    def dump_used_vars(self, context, used_vars):
        b = []
        for n, var in enumerate(used_vars):
            assert isinstance(var, Variable)

            if var.type.startswith('Function'):
                b += [
                    'dup',
                    format(n, '04x'),
                    'aload', var.number,
                    'aastore',
                ]
            else:
                b += [
                    'dup',
                    format(n, '04x'),
                    'aload', var.number,
                    'invokestatic', context.constant_pull['Integer.valueOf'],
                    'aastore',
                ]

        return b

    def __len__(self):
        return 7

    @property
    def len(self):
        return sum(len(i) for i in self.body)

    def r(self, context):
        return list(itertools.chain(*[i.resolve(context) for i in self.body]))

    def resolve(self, context):

        return [
            'sipush', format(len(self.used_vars) + 1, '04x'),
            'anewarray', context.constant_pull['Object class'],
            'astore', self.var.number
        ]


class FunctionCallStatement(Statement):
    def __init__(self, context, name, parameters, position):
        super().__init__(context, 'void', position)
        sp = name + '(' + ','.join(e.type for e in parameters) + ')'
        self.signature = sp + '->?'

        print(self.signature)
        print(context.variables)

    def __len__(self):
        return 4

    def resolve(self, context):
        return [
            'iconst_0',
            'jsr', 'f_call_w2',
        ]


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


class PrintStatement(Statement):
    def __init__(self, context, expr, position):
        super().__init__(context, 'void', position)

        assert isinstance(expr, Statement)
        self.expr = expr

    def __len__(self):
        return len(self.expr) + 3 + 3

    # noinspection PyTypeChecker
    def resolve(self, context):
        return [
                   'getstatic',
                   context.constant_pull['System.out.PrintStream'],
               ] + self.expr.resolve(context) + [
                   'invokevirtual',
                   context.constant_pull['println:(Z)V'] if self.expr.type == 'bool' else context.constant_pull['println:(I)V'],
               ]


class OperatorStatement(Statement):
    BOOLEAN_OPERATORS = {'==', '!=', '&&', 'and', '||', 'or'}
    RETURNS_BOOLEAN = {'==', '!=', '&&', 'and', '||', 'or', '<', '<=', '>', '>='}
    OP_TO_ASM_MAP = {
        '*': ['imul'],
        '/': ['idiv'],
        '%': ['irem'],
        '+': ['iadd'],
        '-': ['isub'],

        '<':  ['if_icmplt', '0007', 'iconst_0', 'goto', '0004', 'iconst_1'],
        '<=': ['if_icmple', '0007', 'iconst_0', 'goto', '0004', 'iconst_1'],
        '>':  ['if_icmpgt', '0007', 'iconst_0', 'goto', '0004', 'iconst_1'],
        '>=': ['if_icmpge', '0007', 'iconst_0', 'goto', '0004', 'iconst_1'],
        '==': ['if_icmpeq', '0007', 'iconst_0', 'goto', '0004', 'iconst_1'],
        '!=': ['if_icmpne', '0007', 'iconst_0', 'goto', '0004', 'iconst_1'],

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
            context.constant_pull['constant_' + str(self.i)]
        ]


class DeclareVariableStatement(Statement):
    def __init__(self, context, t, name, position):
        super().__init__(context, 'void', position)
        if name in context.variables.current_scope:
            raise self.exception("Variable {} already defined in this scope".format(name))

        context.variables.new(name, t)

    def __len__(self):
        return 0

    def resolve(self, context):
        return []


class GetVariableStatement(Statement):
    def __init__(self, context, name, position):
        super().__init__(context, 'void', position)

        if name not in context.variables:
            raise self.exception("Variable {} is not defined".format(name))
        variable = context.variables[name]
        self._type = variable.type

        self.variable = variable
        self.seq = self.variable.resolve()

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
        self.seq = self.variable.update()

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
        self.seq = self.variable.update()

    def __len__(self):
        return len(self.expr) + len(self.seq)

    def resolve(self, context):
        return self.expr.resolve(context) + \
               self.seq


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
            format(3 + self.fs + 3, '04x'),
        ] + (self.false_seq.resolve(context) if self.false_seq is not None else []) + [
           'goto',
           format(3 + self.ts, '04x'),
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
            format(3 + self.seq_size + 3, '04x'),
        ] + self.seq.resolve(context) + [
           'goto',
           format(256 * 256 - 3 - self.seq_size - self.expr_size, '04x'),
        ]


class ScopeStatement(Statement):
    def __init__(self, context, body, position):
        super().__init__(context, 'void', position)
        self.body = body

    def __len__(self):
        return sum(len(i) for i in self.body)

    def resolve(self, context):
        return list(itertools.chain(*[i.resolve(context) for i in self.body]))


class Variable:
    def __init__(self, t, name, number):
        self.type = t
        self.name = name
        self.number = format(number, '02x')

    def update(self):
        return ['i' + 'store', self.number]

    def resolve(self, _=None):
        return ['i' + 'load', self.number]

    def __str__(self):
        return "({}) {} : {}".format(self.number, self.type, self.name)


class Variables:
    def __init__(self, _, previous):
        # todo count locals
        self._previous = previous
        self._current = {}

    @property
    def current_scope(self):
        return self._current

    def new(self, name, t):
        self._current[name] = Variable(t, name, len(self))
        return self._current[name]

    @property
    def previous(self):
        return self._previous

    def __len__(self):
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
        return '\n'.join(str(x) for x in self._current.values()) + ('----\n' + self._previous if self._previous is not None else '')


class Context:
    def __init__(self, source, cp):
        self.file = None
        self.source = source
        self.constant_pull = cp
        self.variables = Variables(self, None)
        self.functions = dict()
        self.get_stream_size = 32

    def push(self, p):
        self.variables = Variables(self, self.variables)

    def pop(self, p):
        self.variables = self.variables.previous

        if self.variables is None:
            raise CompileError(self, p[0], p[1], 'Unexpectedly empty context')

    def build_functions_table(self):
        number_of_functions = len(self.functions)
        full_bodies_length = sum(f.len + 3 for f in self.functions.values())

        switch_size = 9 + number_of_functions * 8 + full_bodies_length + 2

        self.get_stream_size = switch_size  # todo

        table = ''
        tmp_size = 0
        for n, f in sorted(self.functions.items()):
            table += format(n, '08x')
            tmp_size += f.len + 3
            table += format(9 + 8 * number_of_functions + (full_bodies_length - tmp_size), '08x')

        bodies = []
        tmp_size = full_bodies_length
        for n, f in sorted(self.functions.items()):
            tmp_size -= f.len + 3
            bodies += f.r(self)
            bodies += ['goto', format(tmp_size + 3, '04x')]

        return [
               'goto', format(3 + 3 + switch_size + 2, '04x'),
               'nop', 'nop', 'nop', 'swap',
               # jump here
               'lookupswitch',
               format(switch_size - 2, '08x'),      # def
               format(number_of_functions, '08x'),  # num of functions
               table,
        ] + bodies + [
            'astore_0',
            'ret', '00'
        ]
