import itertools

from compiler import bytemap
from compiler.antlr import CompilerLexer
from compiler.antlr import CompilerParser
from compiler.objects import Context
from compiler.settings import *
import antlr4


def compiler(source):
    # input_ = antlr4.FileStream('antlr/a.txt')
    input_ = antlr4.InputStream(source)

    # input_ = antlr4.InputStream("a=3;\nf(a) { pass; }\n")

    lexer = CompilerLexer.CompilerLexer(input_)
    stream = antlr4.CommonTokenStream(lexer)
    parser = CompilerParser.CompilerParser(stream)

    # rule_name = 'body'
    # tree = getattr(parser, rule_name)()

    c = Context()
    s = parser.body().r

    # print(getMainFunction(parser.functions))

    # create constants
    # calculate function table
    # calculate globals table

    # allocate globals on stack

    # put jmp to globals int to code
    # put functions to code
    # put globals initialization to code

    seq = list(itertools.chain(*[i.resolve(c) for i in s]))
    # print(seq)
    byte_code = bytemap.compile(seq)
    return bytearray(byte_code)
