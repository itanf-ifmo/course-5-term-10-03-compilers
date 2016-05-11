bytecode = [
    ('aaload', '32', 0),
    ('aastore', '53', 0),
    ('aconst_null', '01', 0),
    ('aload', '19', 0),
    ('aload_0', '2a', 0),
    ('aload_1', '2b', 0),
    ('aload_2', '2c', 0),
    ('aload_3', '2d', 0),
    ('anewarray', 'bd', 0),
    ('areturn', 'b0', 0),
    ('arraylength', 'be', 0),
    ('astore', '3a', 0),
    ('astore_0', '4b', 0),
    ('astore_1', '4c', 0),
    ('astore_2', '4d', 0),
    ('astore_3', '4e', 0),
    ('athrow', 'bf', 0),
    ('baload', '33', 0),
    ('bastore', '54', 0),
    ('bipush', '10', 0),
    ('breakpoint', 'ca', 0),
    ('caload', '34', 0),
    ('castore', '55', 0),
    ('checkcast', 'c0', 0),
    ('d2f', '90', 0),
    ('d2i', '8e', 0),
    ('d2l', '8f', 0),
    ('dadd', '63', 0),
    ('daload', '31', 0),
    ('dastore', '52', 0),
    ('dcmpg', '98', 0),
    ('dcmpl', '97', 0),
    ('dconst_0', '0e', 0),
    ('dconst_1', '0f', 0),
    ('ddiv', '6f', 0),
    ('dload', '18', 0),
    ('dload_0', '26', 0),
    ('dload_1', '27', 0),
    ('dload_2', '28', 0),
    ('dload_3', '29', 0),
    ('dmul', '6b', 0),
    ('dneg', '77', 0),
    ('drem', '73', 0),
    ('dreturn', 'af', 0),
    ('dstore', '39', 0),
    ('dstore_0', '47', 0),
    ('dstore_1', '48', 0),
    ('dstore_2', '49', 0),
    ('dstore_3', '4a', 0),
    ('dsub', '67', 0),
    ('dup', '59', 0),
    ('dup_x1', '5a', 0),
    ('dup_x2', '5b', 0),
    ('dup2', '5c', 0),
    ('dup2_x1', '5d', 0),
    ('dup2_x2', '5e', 0),
    ('f2d', '8d', 0),
    ('f2i', '8b', 0),
    ('f2l', '8c', 0),
    ('fadd', '62', 0),
    ('faload', '30', 0),
    ('fastore', '51', 0),
    ('fcmpg', '96', 0),
    ('fcmpl', '95', 0),
    ('fconst_0', '0b', 0),
    ('fconst_1', '0c', 0),
    ('fconst_2', '0d', 0),
    ('fdiv', '6e', 0),
    ('fload', '17', 0),
    ('fload_0', '22', 0),
    ('fload_1', '23', 0),
    ('fload_2', '24', 0),
    ('fload_3', '25', 0),
    ('fmul', '6a', 0),
    ('fneg', '76', 0),
    ('frem', '72', 0),
    ('freturn', 'ae', 0),
    ('fstore', '38', 0),
    ('fstore_0', '43', 0),
    ('fstore_1', '44', 0),
    ('fstore_2', '45', 0),
    ('fstore_3', '46', 0),
    ('fsub', '66', 0),
    ('getfield', 'b4', 0),
    ('getstatic', 'b2', 2),
    ('goto', 'a7', 0),
    ('goto_w', 'c8', 0),
    ('i2b', '91', 0),
    ('i2c', '92', 0),
    ('i2d', '87', 0),
    ('i2f', '86', 0),
    ('i2l', '85', 0),
    ('i2s', '93', 0),
    ('iadd', '60', 0),
    ('iaload', '2e', 0),
    ('iand', '7e', 0),
    ('iastore', '4f', 0),
    ('iconst_m1', '02', 0),
    ('iconst_0', '03', 0),
    ('iconst_1', '04', 0),
    ('iconst_2', '05', 0),
    ('iconst_3', '06', 0),
    ('iconst_4', '07', 0),
    ('iconst_5', '08', 0),
    ('idiv', '6c', 0),
    ('if_acmpeq', 'a5', 0),
    ('if_acmpne', 'a6', 0),
    ('if_icmpeq', '9f', 0),
    ('if_icmpge', 'a2', 0),
    ('if_icmpgt', 'a3', 0),
    ('if_icmple', 'a4', 0),
    ('if_icmplt', 'a1', 0),
    ('if_icmpne', 'a0', 0),
    ('ifeq', '99', 0),
    ('ifge', '9c', 0),
    ('ifgt', '9d', 0),
    ('ifle', '9e', 0),
    ('iflt', '9b', 0),
    ('ifne', '9a', 0),
    ('ifnonnull', 'c7', 0),
    ('ifnull', 'c6', 0),
    ('iinc', '84', 0),
    ('iload', '15', 0),
    ('iload_0', '1a', 0),
    ('iload_1', '1b', 0),
    ('iload_2', '1c', 0),
    ('iload_3', '1d', 0),
    ('impdep1', 'fe', 0),
    ('impdep2', 'ff', 0),
    ('imul', '68', 0),
    ('ineg', '74', 0),
    ('instanceof', 'c1', 0),
    ('invokedynamic', 'ba', 0),
    ('invokeinterface', 'b9', 0),
    ('invokespecial', 'b7', 0),
    ('invokestatic', 'b8', 0),
    ('invokevirtual', 'b6', 2),
    ('ior', '80', 0),
    ('irem', '70', 0),
    ('ireturn', 'ac', 0),
    ('ishl', '78', 0),
    ('ishr', '7a', 0),
    ('istore', '36', 0),
    ('istore_0', '3b', 0),
    ('istore_1', '3c', 0),
    ('istore_2', '3d', 0),
    ('istore_3', '3e', 0),
    ('isub', '64', 0),
    ('iushr', '7c', 0),
    ('ixor', '82', 0),
    ('jsr', 'a8', 0),
    ('jsr_w', 'c9', 0),
    ('l2d', '8a', 0),
    ('l2f', '89', 0),
    ('l2i', '88', 0),
    ('ladd', '61', 0),
    ('laload', '2f', 0),
    ('land', '7f', 0),
    ('lastore', '50', 0),
    ('lcmp', '94', 0),
    ('lconst_0', '09', 0),
    ('lconst_1', '0a', 0),
    ('ldc', '12', 0),
    ('ldc_w', '13', 0),
    ('ldc2_w', '14', 0),
    ('ldiv', '6d', 0),
    ('lload', '16', 0),
    ('lload_0', '1e', 0),
    ('lload_1', '1f', 0),
    ('lload_2', '20', 0),
    ('lload_3', '21', 0),
    ('lmul', '69', 0),
    ('lneg', '75', 0),
    ('lookupswitch', 'ab', 0),
    ('lor', '81', 0),
    ('lrem', '71', 0),
    ('lreturn', 'ad', 0),
    ('lshl', '79', 0),
    ('lshr', '7b', 0),
    ('lstore', '37', 0),
    ('lstore_0', '3f', 0),
    ('lstore_1', '40', 0),
    ('lstore_2', '41', 0),
    ('lstore_3', '42', 0),
    ('lsub', '65', 0),
    ('lushr', '7d', 0),
    ('lxor', '83', 0),
    ('monitorenter', 'c2', 0),
    ('monitorexit', 'c3', 0),
    ('multianewarray', 'c5', 0),
    ('new', 'bb', 0),
    ('newarray', 'bc', 0),
    ('nop', '00', 0),
    ('pop', '57', 0),
    ('pop2', '58', 0),
    ('putfield', 'b5', 0),
    ('putstatic', 'b3', 0),
    ('ret', 'a9', 0),
    ('return', 'b1', 0),
    ('saload', '35', 0),
    ('sastore', '56', 0),
    ('sipush', '11', 0),
    ('swap', '5f', 0),
    ('tableswitch', 'aa', 0),
    ('wide', 'c4', 0)
]


class ConstantPull:
    def __init__(self):
        self.pull = {}

    def __setitem__(self, key, value):
        if isinstance(value, str):
            v = '01{}{}'.format(format(len(value), '04x'), ''.join(format(i, '02x') for i in value.encode()))
        elif isinstance(value, int):
            if value < 0:
                v = '03' + format(256 * 256 * 256 * 256 + value, '08x')
            else:
                v = '03' + format(value, '08x')
        else:
            v = format(value[0], '02x') + ''.join(i for i in value[1:])

        if key in self.pull:
            self.pull[key] = (self.pull[key][0], v)
        else:
            self.pull[key] = (len(self.pull), v)

    def __getitem__(self, item):
        return format(self.pull[item][0] + 1, '04x')

    def putMethodref(self, name, a, b):
        self[name] = [0x0a, self[a], self[b]]

    def putClass(self, name, a):
        self[name] = [0x07, self[a]]

    def putNameAndType(self, name, a, b):
        self[name] = [0x0c, self[a], self[b]]

    def putFieldref(self, name, a, b):
        self[name] = [0x09, self[a], self[b]]

    def __len__(self):
        return len(self.pull) + 1

    def __str__(self):
        return ''.join(v for n, v in sorted(self.pull.values()))

    def createMethodRef(self, alias, method):
        c, other = method.split('.')
        m, t = other.split(':')

        if c + ' string' not in self.pull:
            self[c + ' string'] = c

        if c + ' class' not in self.pull:
            self.putClass(c + ' class', c + ' string')

        if m + ' string' not in self.pull:
            self[m + ' string'] = m

        if t + ' type' not in self.pull:
            self[t + ' type'] = t

        if m + ':' + t not in self.pull:
            self.putNameAndType(m + ':' + t, m + ' string', t + ' type')

        if c + '.' + m + ':' + t not in self.pull:
            self.putMethodref(c + '.' + m + ':' + t, c + ' class', m + ':' + t)

        if alias not in self.pull:
            self.putMethodref(alias, c + ' class', m + ':' + t)


class ByteCodeGenerator:
    def __init__(self, context, instr, sseq='1000'):
        self.ctx = context
        self.cp = self.ctx.constant_pull
        self.seq = processAsm([
            'sipush', '00', '00',
            'istore_1',
            'getstatic', self.cp['st'], '',
            'astore_2',
        ]) + instr + 'b1'
        self.sseq = sseq
        self.max_stack = 1000
        self.max_locals = self.ctx.vars_number
        self.max_args = self.ctx.max_arguments

    def generate(self):
        code = ''
        code += 'cafebabe'  # magic
        code += '0000002f'  # minor_version, major_version
        # code += '0000 0034'  # minor_version, major_version
        code += format(len(self.cp), '04x')
        code += str(self.cp)
        code += '0021'  # access_flags
        code += self.cp['this class']  # this_class
        code += self.cp['Object class']  # super_class
        code += '0000'  # interfaces_count

        code += self._generate_fields()

        code += '0003'  # methods_count

        # main method
        code += '0009'  # mask
        code += self.cp['main method name']
        code += self.cp['main method type']
        code += '0001'  # one attribute
        code += self.cp['code section']
        code += self._generate_code_section()

        # static init
        code += self._generate_static_init_method()

        # switch method
        code += self._generate_switch_method()

        code += '0000'  # class attributes_count

        return [int(i + j, 16) for i, j in list(zip(code[::2], code[1::2]))]

    def _generate_fields(self):
        code = '0002'  # fields_count

        code += '001a'  # ACC_PRIVATE, ACC_STATIC, ACC_FINAL
        code += self.cp['String: stack']  # name: stack
        code += self.cp['[I']  # type: [ I
        code += '0000'  # attributes_count

        code += '001a'  # ACC_PRIVATE, ACC_STATIC, ACC_FINAL
        code += self.cp['String: args_stack']  # name: stack
        code += self.cp['[I']  # type: [ I
        code += '0000'  # attributes_count
        return code

    def _generate_static_init_method(self):
        m = '0008'  # ACC_STATIC
        m += self.cp['<clinit>']  # name: stack
        m += self.cp['()V']  # type: [ I
        m += '0001'  # attributes_count

        m += self.cp['code section']

        code = ''
        code += format(1, '04x')
        code += format(0, '04x')

        seq = processAsm([
            'sipush', format(self.max_locals, '04x'),
            'newarray', '0a',
            'putstatic', self.cp['st'],

            'sipush', format(self.max_args, '04x'),
            'newarray', '0a',
            'putstatic', self.cp['args_st'],

            'return'
        ])

        code += format(len(seq) // 2, '08x')  # code size
        code += seq
        code += '0000'  # ??
        code += '0000'  # no attributes

        m += format(len(code) // 2, '08x') + code

        return m

    def _generate_switch_method(self):
        m = '000a'  # ACC_PRIVATE, ACC_STATIC
        m += self.cp['sw']
        m += self.cp['(I)I']
        m += '0001'  # attributes_count

        m += self.cp['code section']

        code = ''
        code += format(self.max_stack, '04x')
        code += format(4, '04x')

        code += format(len(self.sseq) // 2, '08x')  # code size
        code += self.sseq
        code += '0000'  # ??
        code += '0000'  # no attributes

        m += format(len(code) // 2, '08x') + code

        return m

    def _generate_code_section(self):
        code_section = ''
        code_section += format(self.max_stack, '04x')
        code_section += format(4, '04x')
        code_section += format(len(self.seq) // 2, '08x')  # code size
        code_section += self.seq
        code_section += '0000'  # ??
        code_section += '0000'  # no attributes

        return format(len(code_section) // 2, '08x') + code_section


toAsm = {}
toByte = {}
for i, b, a in bytecode:
    toAsm[int(b, 16)] = (i, a)
    toByte[i] = int(b, 16)


def processAsm(seq):
    res = ''

    current_position = 0
    labels = dict()

    for s in seq:
        if isinstance(s, str) and s.startswith(':'):
            labels[s[1:]] = current_position

        elif isinstance(s, str) and s.startswith('#'):
            current_position += 2

        elif s not in toByte:
            current_position += len(s) // 2
        else:
            current_position += 1

    current_position = 0

    for s in seq:
        if isinstance(s, str) and s.startswith(':'):
            res += '00'

        elif isinstance(s, str) and s.startswith('#'):
            res += format((256 * 256 + (labels[s[1:]] - current_position)) % (256 * 256), '04x')
            current_position += 2

        elif s not in toByte:
            res += s
            current_position += len(s) // 2
        else:
            res += format(toByte[s], '02x')
            current_position += 1

    return res


def compile(c, seq, sseq):
    return ByteCodeGenerator(c, processAsm(seq), processAsm(sseq)).generate()
