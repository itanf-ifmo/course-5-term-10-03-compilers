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


class ByteCodeGenerator:
    @staticmethod
    def _generate_constant_string(s):
        return '01{}{}'.format(format(len(s), '04x'), ''.join(format(i, '02x') for i in s.encode()))

    def __init__(self, programName, instr):
        self.programName = programName
        self.instr = instr

    def generate(self):
        code = ''
        code += 'cafe babe'  # magic
        code += '0000 0034'  # minor_version, major_version
        code += self._generate_constant_pull()
        code += '0020'  # access_flags
        code += '0006'  # this_class (link to constant)
        code += '0007'  # super_class (link to constant)
        code += '0000'  # interfaces_count
        code += '0000'  # fields_count
        code += '0001'  # methods_count (constructor + main)
        code += ''

        code += getCode(self.instr)

        r = code.replace('\n', '').replace(' ', '')
        return [int(i + j, 16) for i, j in list(zip(r[::2], r[1::2]))]

    def _generate_constant_pull(self):
        pull = [
            '0a 0007 0012',
            '09 0013 0014',
            '0a 0015 0016',
            '09 0013 0017',
            '0a 0018 0019',
            '07 001a',
            '07 001b',
            self._generate_constant_string('<init>'),
            self._generate_constant_string('()V'),
            self._generate_constant_string('Code'),
            self._generate_constant_string('LineNumberTable'),
            self._generate_constant_string('main'),
            self._generate_constant_string('([Ljava/lang/String;)V'),
            self._generate_constant_string('Exceptions'),
            '07 001c',
            self._generate_constant_string('SourceFile'),
            self._generate_constant_string('A.java'),
            '0c 0008 0009',
            '07 001d',
            '0c 001e 001f',
            '07 0020',
            '0c 0021 0022',
            '0c 0023 0024',
            '07 0025',
            '0c 0026 0027',
            self._generate_constant_string(self.programName),
            self._generate_constant_string('java/lang/Object'),
            self._generate_constant_string('java/io/IOException'),
            self._generate_constant_string('java/lang/System'),
            self._generate_constant_string('in'),
            self._generate_constant_string('Ljava/io/InputStream;'),
            self._generate_constant_string('java/io/InputStream'),
            self._generate_constant_string('read'),
            self._generate_constant_string('()I'),
            self._generate_constant_string('out'),
            self._generate_constant_string('Ljava/io/PrintStream;'),
            self._generate_constant_string('java/io/PrintStream'),
            self._generate_constant_string('println'),
            self._generate_constant_string('(I)V'),
        ]

        code = ''
        code += format(len(pull) + 1, '04x')  # pull size + 1
        code += ''.join(c for c in pull)
        return code


def getCode(instr):
    i = instr.replace('\n', '').replace(' ', '') + 'b1'
    l = int(len(i) / 2)
    # print(l, format(24 + l, '04x'), format(l, '04x'))

    r = """
0009
000c
000d
0001
    000a     %s
        0003 0005 %s
         %s
        0000
        0000

0000

""" % (format(12 + l, '08x'), format(l, '08x'), i)
    return r


toAsm = {}
tyByte = {}
for i, b, a in bytecode:
    toAsm[int(b, 16)] = (i, a)
    tyByte[i] = int(b, 16)
#
# open('/tmp/A.class', 'bw').write(bytearray(getCode(m)))
# os.system("cd /tmp; java A <<< 23")
# print()
#
#
# m = list(m.replace('\n', '').replace(' ', ''))
# m = list(int(i + j, 16) for i, j in list(zip(m[::2], m[1::2])))
# l = []
# while m:
#     a = m.pop(0)
#     r = d.get(a, ('!' + str(a), 0))
#     args = []
#     if r[1]:
#         for i in range(r[1]):
#             args.append(str(hex(m.pop(0))))
#
#     print(hex(a), r[0], ('(' + ','.join(args) + ')' if args else ''))


def processAsm(seq):
    return [tyByte.get(s, s) for s in seq]


def compile(seq):
    return ByteCodeGenerator('A', ''.join(format(i, '02x') for i in processAsm(seq))).generate()
