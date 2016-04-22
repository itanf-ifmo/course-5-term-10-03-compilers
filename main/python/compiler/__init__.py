import os

from compiler import bytemap
from compiler.antlr import CompilerParser
from compiler.bytemap import ConstantPull
from compiler.objects import Context, CompileError
from compiler.settings import *


def _compiler(source, name='A', file_name=None):
    cp = ConstantPull()
    cp['code section'] = 'Code'
    cp['StackMapTable section'] = 'StackMapTable'
    cp['this class name'] = name
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

    cp['InputStream class name'] = 'java/io/InputStream'
    cp.putClass('InputStream class', 'InputStream class name')
    cp['read'] = 'read'
    cp['()I'] = '()I'
    cp.putNameAndType('read()I', 'read', '()I')
    cp.putMethodref('read:()I', 'InputStream class', 'read()I')

    cp['PrintStream class name'] = 'java/io/PrintStream'
    cp.putClass('PrintStream class', 'PrintStream class name')
    cp['println'] = 'println'

    cp['(I)V'] = '(I)V'
    cp.putNameAndType('println(I)V', 'println', '(I)V')
    cp.putMethodref('println:(I)V', 'PrintStream class', 'println(I)V')

    cp['(Z)V'] = '(Z)V'
    cp.putNameAndType('println(Z)V', 'println', '(Z)V')
    cp.putMethodref('println:(Z)V', 'PrintStream class', 'println(Z)V')

    cp['String: stack'] = 'stack'
    cp['[I'] = '[I'

    cp['<clinit>'] = '<clinit>'
    cp['()V'] = '()V'

    cp.putNameAndType('stack:[I', 'String: stack', '[I')
    cp.putFieldref('Field stack', 'this class', 'stack:[I')
    cp.putFieldref('st', 'this class', 'stack:[I')

    cp['sw'] = 'sw'
    cp['(II)I'] = '(II)I'
    cp.putNameAndType('sw(II)I', 'sw', '(II)I')
    cp.putMethodref('sw:(II)I', 'this class', 'sw(II)I')

    # cp['Integer class name'] = 'java/lang/Integer'
    # cp.putClass('Integer class', 'Integer class name')

    # cp['valueOf'] = 'valueOf'
    # cp['(I)Ljava/lang/Integer'] = '(I)Ljava/lang/Integer'
    # cp.putNameAndType('valueOf:(I)Ljava/lang/Integer', 'valueOf', '(I)Ljava/lang/Integer')
    # cp.putMethodref('Integer.valueOf', 'Integer class', 'valueOf:(I)Ljava/lang/Integer')

    c = Context(source, cp)
    c.file = file_name

    seq = CompilerParser.CompilerParser.parse(source, c)
    byte_code = bytemap.compile(c, seq, c.build_functions_table())
    return bytearray(byte_code)


def build(path_to_file):
    d = os.path.dirname(path_to_file)
    n = '.'.join(os.path.basename(path_to_file).split('.')[:-1])
    data = _compiler(open(path_to_file, 'r').read(), n, path_to_file)
    open(os.path.join(d, n + '.class'), 'wb').write(data)
