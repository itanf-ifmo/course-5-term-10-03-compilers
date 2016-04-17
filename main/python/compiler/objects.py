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
                   context.constant_pull['System.out.PrintStream'],
               ] + self.expr.resolve(context) + [
                   'invokevirtual',
                   context.constant_pull['println:(Z)V'] if self.expr.type == 'bool' else context.constant_pull['println:(I)V'],
               ]


class OperatorStatement(Statement):
    BOOLEAN_OPERATORS = {'==', '!=', '&&', 'and', '||', 'or'}
    OP_TO_ASM_MAP = {
        '*': 'imul',
        '/': 'idiv',
        '%': 'irem',
        '+': 'iadd',
        '-': 'isub',
        '<': '',
        '<=': '',
        '>': '',  # todo
        '>=': '',
        '==': '',
        '!=': '',
        '&&': 'iand',
        'and': 'iand',
        '||': 'ior',
        'or': 'ior',
    }

    def __init__(self, expr1, op, expr2, position):
        super().__init__('bool' if op in self.BOOLEAN_OPERATORS else expr1.type, position)
        assert isinstance(expr1, Statement)
        assert isinstance(expr2, Statement)

        if expr1.type != expr2.type and op not in self.BOOLEAN_OPERATORS:
            raise self.exception("Type of operand mismatches: {} {} {}".format(expr1.type, op, expr2.type))

        if expr1.type == 'bool' and op not in self.BOOLEAN_OPERATORS:
            raise self.exception("Unexpected operator for boolean parameters: {}".format(op))

        self.expr1 = expr1
        self.expr2 = expr2

        self.op = self.OP_TO_ASM_MAP[op]

    def __len__(self):
        return len(self.expr1) + 1 + len(self.expr1)

    # noinspection PyTypeChecker
    def resolve(self, context):
        return self.expr1.resolve(context) + \
               self.expr2.resolve(context) + \
               [self.op]


class UnaryOperatorStatement(Statement):
    BOOLEAN_UNARY_OPERATORS = {'!', 'not'}
    OP_TO_ASM_MAP = {
        '!': ['iconst_1', 'ixor'],
        'not': ['iconst_1', 'ixor'],
        '-': ['ineg'],
    }

    def __init__(self, op, expr, position):
        super().__init__('bool' if op in self.BOOLEAN_UNARY_OPERATORS else expr.type, position)

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
    def __init__(self, i, position):
        super().__init__('int', position)

        self.i = i

    def __len__(self):
        return 3

    def resolve(self, context):
        context.constant_pull['constant_' + str(self.i)] = self.i

        return [
            'ldc_w',
            context.constant_pull['constant_' + str(self.i)]
        ]


class Context:
    def __init__(self, cp):
        self.vars = []
        self.constant_pull = cp

    def resolveFuncCall(self):
        pass

    def resolveVariable(self, var_name):
        for ctx in self.vars:
            if var_name in ctx:
                return ctx[var_name]

        return None
