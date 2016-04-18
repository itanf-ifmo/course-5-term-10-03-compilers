from compiler import bytemap
from compiler.antlr import CompilerParser
from compiler.bytemap import ConstantPull
from compiler.objects import Context, CompileError
from compiler.settings import *


def compiler(source):
    cp = ConstantPull()
    cp['code section'] = 'Code'
    cp['StackMapTable section'] = 'StackMapTable'
    cp['this class name'] = 'A'
    cp['super class name'] = 'java/lang/Object'
    cp.putClass('this class', 'this class name')
    cp.putClass('super class', 'super class name')

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

    c = Context(source, cp)

    # print(getMainFunction(parser.functions))

    # create constants
    # calculate function table
    # calculate globals table

    # allocate globals on stack

    # put jmp to globals int to code
    # put functions to code
    # put globals initialization to code
    seq = CompilerParser.CompilerParser.parse(source, c)
    byte_code = bytemap.compile(cp, seq)
    return bytearray(byte_code)
