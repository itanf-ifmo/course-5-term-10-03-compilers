import os

from compiler import bytemap
from compiler.antlr import CompilerParser
from compiler.bytemap import ConstantPull
from compiler.objects import Context, CompileError
from compiler.settings import *


def _compiler(source, name='A', file_name=None):
    c = Context(name, source)
    c.file = file_name

    seq = CompilerParser.CompilerParser.parse(source, c)
    byte_code = bytemap.compile(c, seq, c.build_functions_table())
    return bytearray(byte_code)


def build(path_to_file):
    d = os.path.dirname(path_to_file)
    n = '.'.join(os.path.basename(path_to_file).split('.')[:-1])

    with open(path_to_file, 'r') as src_file:
        data = _compiler(src_file.read(), n, path_to_file)

    with open(os.path.join(d, n + '.class'), 'wb') as output_file:
        output_file.write(data)
