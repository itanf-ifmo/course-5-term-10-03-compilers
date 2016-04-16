class Function:
    def __init__(self, return_type, name, parameters, body):
        self.return_type = return_type
        self.name = name
        self.parameters = parameters
        self.body = body

        print(self.body)
        self.main = return_type == 'void' and name == 'main' and parameters is None

    def __str__(self):
        return "{} {}({})".format(self.return_type, self.name, self.parameters if self.parameters is not None else '')


class Statement:
    def __init__(self, t, position):
        self._type = t
        self._position = position

    def resolve(self, context):
        return []

    def exception(self, msg):
        return Exception("line:{}, pos:{}   {}".format(self._position[0], self._position[1], msg))

    @property
    def type(self):
        return self._type

    def __len__(self):
        return 0


class BoolStatement(Statement):
    def __init__(self, v, position):
        super().__init__('bool', position)

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
    def __init__(self, expr, position):
        super().__init__('print', position)

        assert isinstance(expr, Statement)
        self.expr = expr

    def __len__(self):
        return len(self.expr) + 3 + 3

    # noinspection PyTypeChecker
    def resolve(self, context):
        return [
                   'getstatic',
                   context.constants['GET_STATIC_PRINT'][0],
                   context.constants['GET_STATIC_PRINT'][1],
               ] + self.expr.resolve(context) + [
                   'invokevirtual',
                   context.constants['INVOKE_VIRTUAL_PRINT_INT'][0],
                   context.constants['INVOKE_VIRTUAL_PRINT_INT'][1],
               ]


class OperatorStatement(Statement):
    BOOLEAN_OPERATORS = {'==', '!=', '&&', 'and', '||', 'or'}
    OP_TO_ASM_MAP = {
        '*': '',  # todo
        '/': '',
        '%': '',
        '+': '',
        '-': '',
        '<': '',
        '<=': '',
        '>': '',
        '>=': '',
        '==': '',
        '!=': '',
        '&&': '',
        'and': '',
        '||': '',
        'or': '',
    }

    def __init__(self, expr1, op, expr2, position):

        if expr1.type != expr2.type:
            raise self.exception("Type of operand mismatches: {} {} {}".format(expr1, op, expr2))

        if expr1.type == 'bool' and op not in self.BOOLEAN_OPERATORS:
            raise self.exception("Unexpected operator for boolean parameters: {}".format(op))

        super().__init__(expr1.type, position)
        assert isinstance(expr1, Statement)
        assert isinstance(expr2, Statement)

        self.expr1 = expr1
        self.expr2 = expr2

        self.op = self.OP_TO_ASM_MAP[op]

    def __len__(self):
        return len(self.expr1) + 1 + len(self.expr1)

    # noinspection PyTypeChecker
    def resolve(self, context):
        return self.expr1.resolve(context) + \
               self.expr2.resolve(context) + \
               self.op


class UnaryOperatorStatement(Statement):
    BOOLEAN_UNARY_OPERATORS = {'!', 'not'}
    OP_TO_ASM_MAP = {
        '!': ['iconst_1', 'ixor'],
        'not': ['iconst_1', 'ixor'],
        '-': ['ineg'],
    }

    def __init__(self, op, expr, position):
        if expr.type == 'bool' and op not in self.BOOLEAN_UNARY_OPERATORS:
            raise self.exception("Unexpected unary operator for boolean expression: {}".format(self.op))

        super().__init__('unary', position)
        assert isinstance(expr, Statement)

        self.expr = expr
        self.op = self.OP_TO_ASM_MAP[op]

    def __len__(self):
        return len(self.expr) + len(self.op)

    def resolve(self, context):
        return self.expr.resolve(context) + \
               self.op


class Context:
    def __init__(self):
        self.vars = []
        self.constants = {
            'GET_STATIC_PRINT': [0x0, 0x4],
            'INVOKE_VIRTUAL_PRINT_INT': [0x0, 0x5],
        }

    def resolveFuncCall(self):
        pass

    def resolveVariable(self, var_name):
        for ctx in self.vars:
            if var_name in ctx:
                return ctx[var_name]

        return None
