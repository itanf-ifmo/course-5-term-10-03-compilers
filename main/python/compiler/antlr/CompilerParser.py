# Generated from ./antlr/Compiler.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO


from compiler.objects import *
from compiler.antlr import CompilerLexer
import itertools
import antlr4
from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def __init__(self, context):
        super(MyErrorListener, self).__init__()
        self._context = context

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseError(self._context, line, column, msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3-")
        buf.write("\u015d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\5\2F\n\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\7\2j\n\2\f\2\16\2m\13\2\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5{\n\5\3\5\3\5\3\5\3\5\7")
        buf.write("\5\u0081\n\5\f\5\16\5\u0084\13\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\5\b\u009c\n\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t")
        buf.write("\u00a4\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u00c3\n\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\5\13\u00cb\n\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00d3")
        buf.write("\n\f\f\f\16\f\u00d6\13\f\3\f\5\f\u00d9\n\f\5\f\u00db\n")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e5\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00f0\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00fc\n\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u011e\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\5\24\u0125\n\24\3\24\3\24\3\24\3\24\3\24\7\24\u012c")
        buf.write("\n\24\f\24\16\24\u012f\13\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0139\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u0142\n\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u014a\n\27\3\27\3\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u0152\n\27\7\27\u0154\n\27\f\27\16\27\u0157\13\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\2\3\2\30\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,\2\t\3\2\20\21\3\2\6\b\4\2\5")
        buf.write("\5\t\t\3\2\n\r\3\2\16\17\3\2\22\23\3\2\24\25\u0172\2E")
        buf.write("\3\2\2\2\4n\3\2\2\2\6r\3\2\2\2\bv\3\2\2\2\n\u0088\3\2")
        buf.write("\2\2\f\u008e\3\2\2\2\16\u009b\3\2\2\2\20\u00a3\3\2\2\2")
        buf.write("\22\u00c2\3\2\2\2\24\u00ca\3\2\2\2\26\u00da\3\2\2\2\30")
        buf.write("\u00e4\3\2\2\2\32\u00ef\3\2\2\2\34\u00fb\3\2\2\2\36\u00fd")
        buf.write("\3\2\2\2 \u0101\3\2\2\2\"\u010c\3\2\2\2$\u011d\3\2\2\2")
        buf.write("&\u011f\3\2\2\2(\u0138\3\2\2\2*\u0141\3\2\2\2,\u0143\3")
        buf.write("\2\2\2./\b\2\1\2/\60\7&\2\2\60F\b\2\1\2\61\62\7)\2\2\62")
        buf.write("F\b\2\1\2\63\64\5\4\3\2\64\65\b\2\1\2\65F\3\2\2\2\66\67")
        buf.write("\7\3\2\2\678\5\2\2\289\7\4\2\29:\b\2\1\2:F\3\2\2\2;<\7")
        buf.write("*\2\2<F\b\2\1\2=>\7\5\2\2>?\5\2\2\n?@\b\2\1\2@F\3\2\2")
        buf.write("\2AB\t\2\2\2BC\5\2\2\5CD\b\2\1\2DF\3\2\2\2E.\3\2\2\2E")
        buf.write("\61\3\2\2\2E\63\3\2\2\2E\66\3\2\2\2E;\3\2\2\2E=\3\2\2")
        buf.write("\2EA\3\2\2\2Fk\3\2\2\2GH\f\t\2\2HI\t\3\2\2IJ\5\2\2\nJ")
        buf.write("K\b\2\1\2Kj\3\2\2\2LM\f\b\2\2MN\t\4\2\2NO\5\2\2\tOP\b")
        buf.write("\2\1\2Pj\3\2\2\2QR\f\7\2\2RS\t\5\2\2ST\5\2\2\bTU\b\2\1")
        buf.write("\2Uj\3\2\2\2VW\f\6\2\2WX\t\6\2\2XY\5\2\2\7YZ\b\2\1\2Z")
        buf.write("j\3\2\2\2[\\\f\4\2\2\\]\t\7\2\2]^\5\2\2\5^_\b\2\1\2_j")
        buf.write("\3\2\2\2`a\f\3\2\2ab\t\b\2\2bc\5\2\2\4cd\b\2\1\2dj\3\2")
        buf.write("\2\2ef\f\13\2\2fg\5\b\5\2gh\b\2\1\2hj\3\2\2\2iG\3\2\2")
        buf.write("\2iL\3\2\2\2iQ\3\2\2\2iV\3\2\2\2i[\3\2\2\2i`\3\2\2\2i")
        buf.write("e\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2l\3\3\2\2\2mk\3")
        buf.write("\2\2\2no\7*\2\2op\5\b\5\2pq\b\3\1\2q\5\3\2\2\2rs\5\2\2")
        buf.write("\2st\5\b\5\2tu\b\4\1\2u\7\3\2\2\2vz\7\3\2\2wx\5\2\2\2")
        buf.write("xy\b\5\1\2y{\3\2\2\2zw\3\2\2\2z{\3\2\2\2{\u0082\3\2\2")
        buf.write("\2|}\7\'\2\2}~\5\2\2\2~\177\b\5\1\2\177\u0081\3\2\2\2")
        buf.write("\u0080|\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2")
        buf.write("\2\u0082\u0083\3\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0085\u0086\7\4\2\2\u0086\u0087\b\5\1\2\u0087")
        buf.write("\t\3\2\2\2\u0088\u0089\5*\26\2\u0089\u008a\7*\2\2\u008a")
        buf.write("\u008b\7\26\2\2\u008b\u008c\5\2\2\2\u008c\u008d\b\6\1")
        buf.write("\2\u008d\13\3\2\2\2\u008e\u008f\7*\2\2\u008f\u0090\7\26")
        buf.write("\2\2\u0090\u0091\5\2\2\2\u0091\u0092\b\7\1\2\u0092\r\3")
        buf.write("\2\2\2\u0093\u0094\5\2\2\2\u0094\u0095\7\27\2\2\u0095")
        buf.write("\u0096\b\b\1\2\u0096\u009c\3\2\2\2\u0097\u0098\7\30\2")
        buf.write("\2\u0098\u0099\5\2\2\2\u0099\u009a\b\b\1\2\u009a\u009c")
        buf.write("\3\2\2\2\u009b\u0093\3\2\2\2\u009b\u0097\3\2\2\2\u009c")
        buf.write("\17\3\2\2\2\u009d\u009e\7\27\2\2\u009e\u009f\7*\2\2\u009f")
        buf.write("\u00a4\b\t\1\2\u00a0\u00a1\7\31\2\2\u00a1\u00a2\7*\2\2")
        buf.write("\u00a2\u00a4\b\t\1\2\u00a3\u009d\3\2\2\2\u00a3\u00a0\3")
        buf.write("\2\2\2\u00a4\21\3\2\2\2\u00a5\u00a6\5\f\7\2\u00a6\u00a7")
        buf.write("\b\n\1\2\u00a7\u00c3\3\2\2\2\u00a8\u00a9\5\16\b\2\u00a9")
        buf.write("\u00aa\b\n\1\2\u00aa\u00c3\3\2\2\2\u00ab\u00ac\5\20\t")
        buf.write("\2\u00ac\u00ad\b\n\1\2\u00ad\u00c3\3\2\2\2\u00ae\u00af")
        buf.write("\5\34\17\2\u00af\u00b0\b\n\1\2\u00b0\u00c3\3\2\2\2\u00b1")
        buf.write("\u00b2\5$\23\2\u00b2\u00b3\b\n\1\2\u00b3\u00c3\3\2\2\2")
        buf.write("\u00b4\u00b5\5\"\22\2\u00b5\u00b6\b\n\1\2\u00b6\u00c3")
        buf.write("\3\2\2\2\u00b7\u00b8\5\4\3\2\u00b8\u00b9\b\n\1\2\u00b9")
        buf.write("\u00c3\3\2\2\2\u00ba\u00bb\5\6\4\2\u00bb\u00bc\b\n\1\2")
        buf.write("\u00bc\u00c3\3\2\2\2\u00bd\u00be\7(\2\2\u00be\u00c3\b")
        buf.write("\n\1\2\u00bf\u00c0\5\24\13\2\u00c0\u00c1\b\n\1\2\u00c1")
        buf.write("\u00c3\3\2\2\2\u00c2\u00a5\3\2\2\2\u00c2\u00a8\3\2\2\2")
        buf.write("\u00c2\u00ab\3\2\2\2\u00c2\u00ae\3\2\2\2\u00c2\u00b1\3")
        buf.write("\2\2\2\u00c2\u00b4\3\2\2\2\u00c2\u00b7\3\2\2\2\u00c2\u00ba")
        buf.write("\3\2\2\2\u00c2\u00bd\3\2\2\2\u00c2\u00bf\3\2\2\2\u00c3")
        buf.write("\23\3\2\2\2\u00c4\u00c5\7\32\2\2\u00c5\u00c6\5\2\2\2\u00c6")
        buf.write("\u00c7\b\13\1\2\u00c7\u00cb\3\2\2\2\u00c8\u00c9\7\32\2")
        buf.write("\2\u00c9\u00cb\b\13\1\2\u00ca\u00c4\3\2\2\2\u00ca\u00c8")
        buf.write("\3\2\2\2\u00cb\25\3\2\2\2\u00cc\u00cd\5\30\r\2\u00cd\u00d4")
        buf.write("\b\f\1\2\u00ce\u00cf\7\33\2\2\u00cf\u00d0\5\30\r\2\u00d0")
        buf.write("\u00d1\b\f\1\2\u00d1\u00d3\3\2\2\2\u00d2\u00ce\3\2\2\2")
        buf.write("\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3")
        buf.write("\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d9")
        buf.write("\7\33\2\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00db\3\2\2\2\u00da\u00cc\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00dd\b\f\1\2\u00dd\27\3\2")
        buf.write("\2\2\u00de\u00df\5\32\16\2\u00df\u00e0\b\r\1\2\u00e0\u00e5")
        buf.write("\3\2\2\2\u00e1\u00e2\5\22\n\2\u00e2\u00e3\b\r\1\2\u00e3")
        buf.write("\u00e5\3\2\2\2\u00e4\u00de\3\2\2\2\u00e4\u00e1\3\2\2\2")
        buf.write("\u00e5\31\3\2\2\2\u00e6\u00e7\5\36\20\2\u00e7\u00e8\b")
        buf.write("\16\1\2\u00e8\u00f0\3\2\2\2\u00e9\u00ea\5\n\6\2\u00ea")
        buf.write("\u00eb\b\16\1\2\u00eb\u00f0\3\2\2\2\u00ec\u00ed\5 \21")
        buf.write("\2\u00ed\u00ee\b\16\1\2\u00ee\u00f0\3\2\2\2\u00ef\u00e6")
        buf.write("\3\2\2\2\u00ef\u00e9\3\2\2\2\u00ef\u00ec\3\2\2\2\u00f0")
        buf.write("\33\3\2\2\2\u00f1\u00f2\7\34\2\2\u00f2\u00f3\7\35\2\2")
        buf.write("\u00f3\u00fc\b\17\1\2\u00f4\u00f5\7\34\2\2\u00f5\u00f6")
        buf.write("\b\17\1\2\u00f6\u00f7\5\26\f\2\u00f7\u00f8\b\17\1\2\u00f8")
        buf.write("\u00f9\7\35\2\2\u00f9\u00fa\b\17\1\2\u00fa\u00fc\3\2\2")
        buf.write("\2\u00fb\u00f1\3\2\2\2\u00fb\u00f4\3\2\2\2\u00fc\35\3")
        buf.write("\2\2\2\u00fd\u00fe\5*\26\2\u00fe\u00ff\7*\2\2\u00ff\u0100")
        buf.write("\b\20\1\2\u0100\37\3\2\2\2\u0101\u0102\5(\25\2\u0102\u0103")
        buf.write("\7*\2\2\u0103\u0104\5&\24\2\u0104\u0105\7\34\2\2\u0105")
        buf.write("\u0106\b\21\1\2\u0106\u0107\b\21\1\2\u0107\u0108\5\26")
        buf.write("\f\2\u0108\u0109\b\21\1\2\u0109\u010a\7\35\2\2\u010a\u010b")
        buf.write("\b\21\1\2\u010b!\3\2\2\2\u010c\u010d\7\36\2\2\u010d\u010e")
        buf.write("\5\2\2\2\u010e\u010f\5\22\n\2\u010f\u0110\b\22\1\2\u0110")
        buf.write("#\3\2\2\2\u0111\u0112\7\37\2\2\u0112\u0113\5\2\2\2\u0113")
        buf.write("\u0114\5\22\n\2\u0114\u0115\7 \2\2\u0115\u0116\5\22\n")
        buf.write("\2\u0116\u0117\b\23\1\2\u0117\u011e\3\2\2\2\u0118\u0119")
        buf.write("\7\37\2\2\u0119\u011a\5\2\2\2\u011a\u011b\5\22\n\2\u011b")
        buf.write("\u011c\b\23\1\2\u011c\u011e\3\2\2\2\u011d\u0111\3\2\2")
        buf.write("\2\u011d\u0118\3\2\2\2\u011e%\3\2\2\2\u011f\u0124\7\3")
        buf.write("\2\2\u0120\u0121\5*\26\2\u0121\u0122\7*\2\2\u0122\u0123")
        buf.write("\b\24\1\2\u0123\u0125\3\2\2\2\u0124\u0120\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125\u012d\3\2\2\2\u0126\u0127\7\'\2\2")
        buf.write("\u0127\u0128\5*\26\2\u0128\u0129\7*\2\2\u0129\u012a\b")
        buf.write("\24\1\2\u012a\u012c\3\2\2\2\u012b\u0126\3\2\2\2\u012c")
        buf.write("\u012f\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2")
        buf.write("\u012e\u0130\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131\7")
        buf.write("\4\2\2\u0131\u0132\b\24\1\2\u0132\'\3\2\2\2\u0133\u0134")
        buf.write("\5*\26\2\u0134\u0135\b\25\1\2\u0135\u0139\3\2\2\2\u0136")
        buf.write("\u0137\7!\2\2\u0137\u0139\b\25\1\2\u0138\u0133\3\2\2\2")
        buf.write("\u0138\u0136\3\2\2\2\u0139)\3\2\2\2\u013a\u013b\7\"\2")
        buf.write("\2\u013b\u0142\b\26\1\2\u013c\u013d\7#\2\2\u013d\u0142")
        buf.write("\b\26\1\2\u013e\u013f\5,\27\2\u013f\u0140\b\26\1\2\u0140")
        buf.write("\u0142\3\2\2\2\u0141\u013a\3\2\2\2\u0141\u013c\3\2\2\2")
        buf.write("\u0141\u013e\3\2\2\2\u0142+\3\2\2\2\u0143\u0149\7\3\2")
        buf.write("\2\u0144\u0145\5*\26\2\u0145\u0146\b\27\1\2\u0146\u014a")
        buf.write("\3\2\2\2\u0147\u0148\7$\2\2\u0148\u014a\b\27\1\2\u0149")
        buf.write("\u0144\3\2\2\2\u0149\u0147\3\2\2\2\u0149\u014a\3\2\2\2")
        buf.write("\u014a\u0155\3\2\2\2\u014b\u0151\7\'\2\2\u014c\u014d\5")
        buf.write("*\26\2\u014d\u014e\b\27\1\2\u014e\u0152\3\2\2\2\u014f")
        buf.write("\u0150\7$\2\2\u0150\u0152\b\27\1\2\u0151\u014c\3\2\2\2")
        buf.write("\u0151\u014f\3\2\2\2\u0152\u0154\3\2\2\2\u0153\u014b\3")
        buf.write("\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0155\3\2\2\2\u0158")
        buf.write("\u0159\7%\2\2\u0159\u015a\5(\25\2\u015a\u015b\b\27\1\2")
        buf.write("\u015b-\3\2\2\2\31Eikz\u0082\u009b\u00a3\u00c2\u00ca\u00d4")
        buf.write("\u00d8\u00da\u00e4\u00ef\u00fb\u011d\u0124\u012d\u0138")
        buf.write("\u0141\u0149\u0151\u0155")
        return buf.getvalue()


class CompilerParser ( Parser ):

    grammarFileName = "Compiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'-'", "'*'", "'/'", "'%'", 
                     "'+'", "'<'", "'<='", "'>'", "'>='", "'=='", "'!='", 
                     "'!'", "'not'", "'&&'", "'and'", "'||'", "'or'", "'='", 
                     "'>>'", "'print'", "'read'", "'return'", "';'", "'{'", 
                     "'}'", "'while'", "'if'", "'else'", "'void'", "'int'", 
                     "'bool'", "'X'", "')->'", "<INVALID>", "','", "'pass'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOL", "COMA", "PASS", "INT", "ID", "COMMENT", "LINE_COMMENT", 
                      "WS" ]

    RULE_expr = 0
    RULE_func_call = 1
    RULE_func_expr_call = 2
    RULE_call_arguments = 3
    RULE_variable_declaration_andassignment = 4
    RULE_assignment = 5
    RULE_write = 6
    RULE_read = 7
    RULE_seq = 8
    RULE_returnW = 9
    RULE_body = 10
    RULE_body_seq = 11
    RULE_declarations = 12
    RULE_scope = 13
    RULE_variable_declaration = 14
    RULE_function_declaration = 15
    RULE_while_expr = 16
    RULE_if_expr = 17
    RULE_function_parameters = 18
    RULE_funcReturnType = 19
    RULE_varType = 20
    RULE_functionalType = 21

    ruleNames =  [ "expr", "func_call", "func_expr_call", "call_arguments", 
                   "variable_declaration_andassignment", "assignment", "write", 
                   "read", "seq", "returnW", "body", "body_seq", "declarations", 
                   "scope", "variable_declaration", "function_declaration", 
                   "while_expr", "if_expr", "function_parameters", "funcReturnType", 
                   "varType", "functionalType" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    BOOL=36
    COMA=37
    PASS=38
    INT=39
    ID=40
    COMMENT=41
    LINE_COMMENT=42
    WS=43

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def setContext(self, context):
        self.context = context

    @staticmethod
    def parse(source, context):
        lexer = CompilerLexer.CompilerLexer(antlr4.InputStream(source))
        lexer._listeners = [ MyErrorListener(context) ]
        stream = antlr4.CommonTokenStream(lexer)
        parser = CompilerParser(stream)
        parser._listeners = [ MyErrorListener(context) ]
        parser.setContext(context)
        return list(itertools.chain(*[i.resolve(context) for i in parser.body().v if i is not None]))


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.e = None # ExprContext
            self.e1 = None # ExprContext
            self.t = None # Token
            self._INT = None # Token
            self._func_call = None # Func_callContext
            self._ID = None # Token
            self.o = None # Token
            self.e2 = None # ExprContext
            self.a = None # Call_argumentsContext

        def BOOL(self):
            return self.getToken(CompilerParser.BOOL, 0)

        def INT(self):
            return self.getToken(CompilerParser.INT, 0)

        def func_call(self):
            return self.getTypedRuleContext(CompilerParser.Func_callContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ExprContext,i)


        def ID(self):
            return self.getToken(CompilerParser.ID, 0)

        def call_arguments(self):
            return self.getTypedRuleContext(CompilerParser.Call_argumentsContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CompilerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 45
                localctx.t = self.match(CompilerParser.BOOL)
                localctx.v = BoolStatement(self.context, (None if localctx.t is None else localctx.t.text) == 'true', ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))
                pass

            elif la_ == 2:
                self.state = 47
                localctx._INT = self.match(CompilerParser.INT)
                localctx.v = ConstIntStatement(self.context, (0 if localctx._INT is None else int(localctx._INT.text)), ((0 if localctx._INT is None else localctx._INT.line), (0 if localctx._INT is None else localctx._INT.column)))
                pass

            elif la_ == 3:
                self.state = 49
                localctx._func_call = self.func_call()
                localctx.v = localctx._func_call.v.call_from_expression()
                pass

            elif la_ == 4:
                self.state = 52
                self.match(CompilerParser.T__0)
                self.state = 53
                localctx.e = self.expr(0)
                self.state = 54
                self.match(CompilerParser.T__1)
                localctx.v=localctx.e.v
                pass

            elif la_ == 5:
                self.state = 57
                localctx._ID = self.match(CompilerParser.ID)
                localctx.v = GetVariableStatement(self.context, (None if localctx._ID is None else localctx._ID.text), ((0 if localctx._ID is None else localctx._ID.line), (0 if localctx._ID is None else localctx._ID.column)))
                pass

            elif la_ == 6:
                self.state = 59
                localctx.o = self.match(CompilerParser.T__2)
                self.state = 60
                localctx.e = self.expr(8)
                localctx.v = UnaryOperatorStatement(self.context, (None if localctx.o is None else localctx.o.text), localctx.e.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                pass

            elif la_ == 7:
                self.state = 63
                localctx.o = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==CompilerParser.T__13 or _la==CompilerParser.T__14):
                    localctx.o = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 64
                localctx.e = self.expr(3)
                localctx.v = UnaryOperatorStatement(self.context, (None if localctx.o is None else localctx.o.text), localctx.e.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CompilerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 70
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CompilerParser.T__3) | (1 << CompilerParser.T__4) | (1 << CompilerParser.T__5))) != 0)):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 71
                        localctx.e2 = self.expr(8)
                        localctx.v = OperatorStatement(self.context, localctx.e1.v, (None if localctx.o is None else localctx.o.text), localctx.e2.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                        pass

                    elif la_ == 2:
                        localctx = CompilerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 75
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CompilerParser.T__2 or _la==CompilerParser.T__6):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 76
                        localctx.e2 = self.expr(7)
                        localctx.v = OperatorStatement(self.context, localctx.e1.v, (None if localctx.o is None else localctx.o.text), localctx.e2.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                        pass

                    elif la_ == 3:
                        localctx = CompilerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 79
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 80
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CompilerParser.T__7) | (1 << CompilerParser.T__8) | (1 << CompilerParser.T__9) | (1 << CompilerParser.T__10))) != 0)):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 81
                        localctx.e2 = self.expr(6)
                        localctx.v = OperatorStatement(self.context, localctx.e1.v, (None if localctx.o is None else localctx.o.text), localctx.e2.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                        pass

                    elif la_ == 4:
                        localctx = CompilerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 85
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CompilerParser.T__11 or _la==CompilerParser.T__12):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 86
                        localctx.e2 = self.expr(5)
                        localctx.v = OperatorStatement(self.context, localctx.e1.v, (None if localctx.o is None else localctx.o.text), localctx.e2.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                        pass

                    elif la_ == 5:
                        localctx = CompilerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 90
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CompilerParser.T__15 or _la==CompilerParser.T__16):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 91
                        localctx.e2 = self.expr(3)
                        localctx.v = OperatorStatement(self.context, localctx.e1.v, (None if localctx.o is None else localctx.o.text), localctx.e2.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                        pass

                    elif la_ == 6:
                        localctx = CompilerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 94
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 95
                        localctx.o = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CompilerParser.T__17 or _la==CompilerParser.T__18):
                            localctx.o = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 96
                        localctx.e2 = self.expr(2)
                        localctx.v = OperatorStatement(self.context, localctx.e1.v, (None if localctx.o is None else localctx.o.text), localctx.e2.v, ((0 if localctx.o is None else localctx.o.line), (0 if localctx.o is None else localctx.o.column)))
                        pass

                    elif la_ == 7:
                        localctx = CompilerParser.ExprContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 99
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 100
                        localctx.a = self.call_arguments()
                        localctx.v = FunctionExprCallStatement(self.context, localctx.e.v, localctx.a.v, localctx.e.v._position).call_from_expression()
                        pass

             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.n = None # Token
            self.a = None # Call_argumentsContext

        def ID(self):
            return self.getToken(CompilerParser.ID, 0)

        def call_arguments(self):
            return self.getTypedRuleContext(CompilerParser.Call_argumentsContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)




    def func_call(self):

        localctx = CompilerParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            localctx.n = self.match(CompilerParser.ID)
            self.state = 109
            localctx.a = self.call_arguments()
            localctx.v = FunctionCallStatement(self.context, (None if localctx.n is None else localctx.n.text), localctx.a.v, ((0 if localctx.n is None else localctx.n.line), (0 if localctx.n is None else localctx.n.column)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_expr_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.e = None # ExprContext
            self.a = None # Call_argumentsContext

        def expr(self):
            return self.getTypedRuleContext(CompilerParser.ExprContext,0)


        def call_arguments(self):
            return self.getTypedRuleContext(CompilerParser.Call_argumentsContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_func_expr_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_expr_call" ):
                listener.enterFunc_expr_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_expr_call" ):
                listener.exitFunc_expr_call(self)




    def func_expr_call(self):

        localctx = CompilerParser.Func_expr_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_expr_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            localctx.e = self.expr(0)
            self.state = 113
            localctx.a = self.call_arguments()
            localctx.v = FunctionExprCallStatement(self.context, localctx.e.v, localctx.a.v, localctx.e.v._position)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Call_argumentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.s =  list()
            self._expr = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(CompilerParser.ExprContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_call_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_arguments" ):
                listener.enterCall_arguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_arguments" ):
                listener.exitCall_arguments(self)




    def call_arguments(self):

        localctx = CompilerParser.Call_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(CompilerParser.T__0)
            self.state = 120
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CompilerParser.T__0) | (1 << CompilerParser.T__2) | (1 << CompilerParser.T__13) | (1 << CompilerParser.T__14) | (1 << CompilerParser.BOOL) | (1 << CompilerParser.INT) | (1 << CompilerParser.ID))) != 0):
                self.state = 117
                localctx._expr = self.expr(0)
                localctx.s.append(localctx._expr.v)


            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CompilerParser.COMA:
                self.state = 122
                self.match(CompilerParser.COMA)
                self.state = 123
                localctx._expr = self.expr(0)
                localctx.s.append(localctx._expr.v)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(CompilerParser.T__1)
            localctx.v=localctx.s
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_declaration_andassignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._varType = None # VarTypeContext
            self.t = None # Token
            self._expr = None # ExprContext

        def varType(self):
            return self.getTypedRuleContext(CompilerParser.VarTypeContext,0)


        def expr(self):
            return self.getTypedRuleContext(CompilerParser.ExprContext,0)


        def ID(self):
            return self.getToken(CompilerParser.ID, 0)

        def getRuleIndex(self):
            return CompilerParser.RULE_variable_declaration_andassignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration_andassignment" ):
                listener.enterVariable_declaration_andassignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration_andassignment" ):
                listener.exitVariable_declaration_andassignment(self)




    def variable_declaration_andassignment(self):

        localctx = CompilerParser.Variable_declaration_andassignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_declaration_andassignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            localctx._varType = self.varType()
            self.state = 135
            localctx.t = self.match(CompilerParser.ID)
            self.state = 136
            self.match(CompilerParser.T__19)
            self.state = 137
            localctx._expr = self.expr(0)
            localctx.v = DeclareAndAssignVariableStatement(self.context, localctx._varType.v, (None if localctx.t is None else localctx.t.text), localctx._expr.v, ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._ID = None # Token
            self.t = None # Token
            self._expr = None # ExprContext

        def ID(self):
            return self.getToken(CompilerParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(CompilerParser.ExprContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = CompilerParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            localctx._ID = self.match(CompilerParser.ID)
            self.state = 141
            localctx.t = self.match(CompilerParser.T__19)
            self.state = 142
            localctx._expr = self.expr(0)
            localctx.v = AssignVariableStatement(self.context, (None if localctx._ID is None else localctx._ID.text), localctx._expr.v, ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._expr = None # ExprContext
            self.t = None # Token

        def expr(self):
            return self.getTypedRuleContext(CompilerParser.ExprContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = CompilerParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_write)
        try:
            self.state = 153
            token = self._input.LA(1)
            if token in [CompilerParser.T__0, CompilerParser.T__2, CompilerParser.T__13, CompilerParser.T__14, CompilerParser.BOOL, CompilerParser.INT, CompilerParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                localctx._expr = self.expr(0)
                self.state = 146
                localctx.t = self.match(CompilerParser.T__20)
                localctx.v = PrintStatement(self.context, localctx._expr.v, ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))

            elif token in [CompilerParser.T__21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                localctx.t = self.match(CompilerParser.T__21)
                self.state = 150
                localctx._expr = self.expr(0)
                localctx.v = PrintStatement(self.context, localctx._expr.v, ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReadContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.t = None # Token
            self._ID = None # Token

        def ID(self):
            return self.getToken(CompilerParser.ID, 0)

        def getRuleIndex(self):
            return CompilerParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = CompilerParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_read)
        try:
            self.state = 161
            token = self._input.LA(1)
            if token in [CompilerParser.T__20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                localctx.t = self.match(CompilerParser.T__20)
                self.state = 156
                localctx._ID = self.match(CompilerParser.ID)
                localctx.v = ReadStatement(self.context, (None if localctx._ID is None else localctx._ID.text), ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))

            elif token in [CompilerParser.T__22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                localctx.t = self.match(CompilerParser.T__22)
                self.state = 159
                localctx._ID = self.match(CompilerParser.ID)
                localctx.v = ReadStatement(self.context, (None if localctx._ID is None else localctx._ID.text), ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SeqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._assignment = None # AssignmentContext
            self._write = None # WriteContext
            self._read = None # ReadContext
            self._scope = None # ScopeContext
            self._if_expr = None # If_exprContext
            self._while_expr = None # While_exprContext
            self._func_call = None # Func_callContext
            self._func_expr_call = None # Func_expr_callContext
            self._PASS = None # Token
            self._returnW = None # ReturnWContext

        def assignment(self):
            return self.getTypedRuleContext(CompilerParser.AssignmentContext,0)


        def write(self):
            return self.getTypedRuleContext(CompilerParser.WriteContext,0)


        def read(self):
            return self.getTypedRuleContext(CompilerParser.ReadContext,0)


        def scope(self):
            return self.getTypedRuleContext(CompilerParser.ScopeContext,0)


        def if_expr(self):
            return self.getTypedRuleContext(CompilerParser.If_exprContext,0)


        def while_expr(self):
            return self.getTypedRuleContext(CompilerParser.While_exprContext,0)


        def func_call(self):
            return self.getTypedRuleContext(CompilerParser.Func_callContext,0)


        def func_expr_call(self):
            return self.getTypedRuleContext(CompilerParser.Func_expr_callContext,0)


        def PASS(self):
            return self.getToken(CompilerParser.PASS, 0)

        def returnW(self):
            return self.getTypedRuleContext(CompilerParser.ReturnWContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq" ):
                listener.enterSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq" ):
                listener.exitSeq(self)




    def seq(self):

        localctx = CompilerParser.SeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_seq)
        try:
            self.state = 192
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                localctx._assignment = self.assignment()
                localctx.v = localctx._assignment.v
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                localctx._write = self.write()
                localctx.v = localctx._write.v
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                localctx._read = self.read()
                localctx.v=localctx._read.v
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                localctx._scope = self.scope()
                localctx.v = localctx._scope.v
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                localctx._if_expr = self.if_expr()
                localctx.v = localctx._if_expr.v
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 178
                localctx._while_expr = self.while_expr()
                localctx.v = localctx._while_expr.v
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 181
                localctx._func_call = self.func_call()
                localctx.v = localctx._func_call.v
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 184
                localctx._func_expr_call = self.func_expr_call()
                localctx.v = localctx._func_expr_call.v
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 187
                localctx._PASS = self.match(CompilerParser.PASS)
                localctx.v = PassStatement(self.context, ((0 if localctx._PASS is None else localctx._PASS.line), (0 if localctx._PASS is None else localctx._PASS.column)))
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 189
                localctx._returnW = self.returnW()
                localctx.v = localctx._returnW.v
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ReturnWContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.t = None # Token
            self.e = None # ExprContext
            self._expr = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(CompilerParser.ExprContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_returnW

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnW" ):
                listener.enterReturnW(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnW" ):
                listener.exitReturnW(self)




    def returnW(self):

        localctx = CompilerParser.ReturnWContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_returnW)
        try:
            self.state = 200
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                localctx.t = self.match(CompilerParser.T__23)
                self.state = 195
                localctx.e = localctx._expr = self.expr(0)
                localctx.v = ReturnStatement(self.context, localctx._expr.v , ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                localctx.t = self.match(CompilerParser.T__23)
                localctx.v = ReturnStatement(self.context, None, ((0 if localctx.t is None else localctx.t.line), (0 if localctx.t is None else localctx.t.column)))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.s =  list()
            self._body_seq = None # Body_seqContext

        def body_seq(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.Body_seqContext)
            else:
                return self.getTypedRuleContext(CompilerParser.Body_seqContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = CompilerParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CompilerParser.T__0) | (1 << CompilerParser.T__2) | (1 << CompilerParser.T__13) | (1 << CompilerParser.T__14) | (1 << CompilerParser.T__20) | (1 << CompilerParser.T__21) | (1 << CompilerParser.T__22) | (1 << CompilerParser.T__23) | (1 << CompilerParser.T__25) | (1 << CompilerParser.T__27) | (1 << CompilerParser.T__28) | (1 << CompilerParser.T__30) | (1 << CompilerParser.T__31) | (1 << CompilerParser.T__32) | (1 << CompilerParser.BOOL) | (1 << CompilerParser.PASS) | (1 << CompilerParser.INT) | (1 << CompilerParser.ID))) != 0):
                self.state = 202
                localctx._body_seq = self.body_seq()
                localctx.s.append(localctx._body_seq.v)
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 204
                        self.match(CompilerParser.T__24)
                        self.state = 205
                        localctx._body_seq = self.body_seq()
                        localctx.s.append(localctx._body_seq.v) 
                    self.state = 212
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 214
                _la = self._input.LA(1)
                if _la==CompilerParser.T__24:
                    self.state = 213
                    self.match(CompilerParser.T__24)




            localctx.v=localctx.s
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Body_seqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._declarations = None # DeclarationsContext
            self._seq = None # SeqContext

        def declarations(self):
            return self.getTypedRuleContext(CompilerParser.DeclarationsContext,0)


        def seq(self):
            return self.getTypedRuleContext(CompilerParser.SeqContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_body_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody_seq" ):
                listener.enterBody_seq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody_seq" ):
                listener.exitBody_seq(self)




    def body_seq(self):

        localctx = CompilerParser.Body_seqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body_seq)
        try:
            self.state = 226
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                localctx._declarations = self.declarations()
                localctx.v = localctx._declarations.v
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                localctx._seq = self.seq()
                localctx.v = localctx._seq.v
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._variable_declaration = None # Variable_declarationContext
            self._variable_declaration_andassignment = None # Variable_declaration_andassignmentContext
            self._function_declaration = None # Function_declarationContext

        def variable_declaration(self):
            return self.getTypedRuleContext(CompilerParser.Variable_declarationContext,0)


        def variable_declaration_andassignment(self):
            return self.getTypedRuleContext(CompilerParser.Variable_declaration_andassignmentContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(CompilerParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_declarations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarations" ):
                listener.enterDeclarations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarations" ):
                listener.exitDeclarations(self)




    def declarations(self):

        localctx = CompilerParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declarations)
        try:
            self.state = 237
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                localctx._variable_declaration = self.variable_declaration()
                localctx.v = localctx._variable_declaration.v
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                localctx._variable_declaration_andassignment = self.variable_declaration_andassignment()
                localctx.v = localctx._variable_declaration_andassignment.v
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                localctx._function_declaration = self.function_declaration()
                localctx.v = localctx._function_declaration.v
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ScopeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.s = None # Token
            self._body = None # BodyContext
            self.e = None # Token

        def body(self):
            return self.getTypedRuleContext(CompilerParser.BodyContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_scope

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScope" ):
                listener.enterScope(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScope" ):
                listener.exitScope(self)




    def scope(self):

        localctx = CompilerParser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_scope)
        try:
            self.state = 249
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                localctx.s = self.match(CompilerParser.T__25)
                self.state = 240
                self.match(CompilerParser.T__26)
                localctx.v=ScopeStatement(self.context, [], ((0 if localctx.s is None else localctx.s.line), (0 if localctx.s is None else localctx.s.column)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                localctx.s = self.match(CompilerParser.T__25)
                self.context.push('s', ((0 if localctx.s is None else localctx.s.line), (0 if localctx.s is None else localctx.s.column)))
                self.state = 244
                localctx._body = self.body()
                localctx.v = ScopeStatement(self.context, localctx._body.v, ((0 if localctx.s is None else localctx.s.line), (0 if localctx.s is None else localctx.s.column)))
                self.state = 246
                localctx.e = self.match(CompilerParser.T__26)
                self.context.pop(((0 if localctx.e is None else localctx.e.line), (0 if localctx.e is None else localctx.e.column)))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.t = None # VarTypeContext
            self._ID = None # Token

        def ID(self):
            return self.getToken(CompilerParser.ID, 0)

        def varType(self):
            return self.getTypedRuleContext(CompilerParser.VarTypeContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)




    def variable_declaration(self):

        localctx = CompilerParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            localctx.t = self.varType()
            self.state = 252
            localctx._ID = self.match(CompilerParser.ID)
            localctx.v = DeclareVariableStatement(self.context, localctx.t.v, (None if localctx._ID is None else localctx._ID.text), ((0 if localctx._ID is None else localctx._ID.line), (0 if localctx._ID is None else localctx._ID.column)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._funcReturnType = None # FuncReturnTypeContext
            self.fn = None # Token
            self._function_parameters = None # Function_parametersContext
            self.s = None # Token
            self._body = None # BodyContext

        def funcReturnType(self):
            return self.getTypedRuleContext(CompilerParser.FuncReturnTypeContext,0)


        def function_parameters(self):
            return self.getTypedRuleContext(CompilerParser.Function_parametersContext,0)


        def body(self):
            return self.getTypedRuleContext(CompilerParser.BodyContext,0)


        def ID(self):
            return self.getToken(CompilerParser.ID, 0)

        def getRuleIndex(self):
            return CompilerParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)




    def function_declaration(self):

        localctx = CompilerParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            localctx._funcReturnType = self.funcReturnType()
            self.state = 256
            localctx.fn = self.match(CompilerParser.ID)
            self.state = 257
            localctx._function_parameters = self.function_parameters()
            self.state = 258
            localctx.s = self.match(CompilerParser.T__25)
            self.context.push('f', ((0 if localctx.s is None else localctx.s.line), (0 if localctx.s is None else localctx.s.column)), localctx._funcReturnType.v)
            self.context.push_func_params(localctx._function_parameters.v)
            self.state = 261
            localctx._body = self.body()
            self.context.pop(((0 if localctx.s is None else localctx.s.line), (0 if localctx.s is None else localctx.s.column)))
            self.state = 263
            self.match(CompilerParser.T__26)
            localctx.v = FunctionStatement(self.context, localctx._funcReturnType.v, (None if localctx.fn is None else localctx.fn.text), localctx._function_parameters.v, localctx._body.v, ((0 if localctx.s is None else localctx.s.line), (0 if localctx.s is None else localctx.s.column)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class While_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.w = None # Token
            self.e = None # ExprContext
            self.s = None # SeqContext

        def expr(self):
            return self.getTypedRuleContext(CompilerParser.ExprContext,0)


        def seq(self):
            return self.getTypedRuleContext(CompilerParser.SeqContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_while_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_expr" ):
                listener.enterWhile_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_expr" ):
                listener.exitWhile_expr(self)




    def while_expr(self):

        localctx = CompilerParser.While_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            localctx.w = self.match(CompilerParser.T__27)
            self.state = 267
            localctx.e = self.expr(0)
            self.state = 268
            localctx.s = self.seq()
            localctx.v = WhileStatement(self.context, localctx.e.v, localctx.s.v, ((0 if localctx.w is None else localctx.w.line), (0 if localctx.w is None else localctx.w.column)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.i = None # Token
            self.e = None # ExprContext
            self.t = None # SeqContext
            self.f = None # SeqContext

        def expr(self):
            return self.getTypedRuleContext(CompilerParser.ExprContext,0)


        def seq(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.SeqContext)
            else:
                return self.getTypedRuleContext(CompilerParser.SeqContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_if_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_expr" ):
                listener.enterIf_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_expr" ):
                listener.exitIf_expr(self)




    def if_expr(self):

        localctx = CompilerParser.If_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_expr)
        try:
            self.state = 283
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                localctx.i = self.match(CompilerParser.T__28)
                self.state = 272
                localctx.e = self.expr(0)
                self.state = 273
                localctx.t = self.seq()
                self.state = 274
                self.match(CompilerParser.T__29)
                self.state = 275
                localctx.f = self.seq()
                localctx.v = IfStatement(self.context, localctx.e.v, localctx.t.v, localctx.f.v, ((0 if localctx.i is None else localctx.i.line), (0 if localctx.i is None else localctx.i.column)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                localctx.i = self.match(CompilerParser.T__28)
                self.state = 279
                localctx.e = self.expr(0)
                self.state = 280
                localctx.t = self.seq()
                localctx.v = IfStatement(self.context, localctx.e.v, localctx.t.v, None, ((0 if localctx.i is None else localctx.i.line), (0 if localctx.i is None else localctx.i.column)))
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.s =  list()
            self._varType = None # VarTypeContext
            self._ID = None # Token

        def varType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.VarTypeContext)
            else:
                return self.getTypedRuleContext(CompilerParser.VarTypeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CompilerParser.ID)
            else:
                return self.getToken(CompilerParser.ID, i)

        def getRuleIndex(self):
            return CompilerParser.RULE_function_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_parameters" ):
                listener.enterFunction_parameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_parameters" ):
                listener.exitFunction_parameters(self)




    def function_parameters(self):

        localctx = CompilerParser.Function_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(CompilerParser.T__0)
            self.state = 290
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CompilerParser.T__0) | (1 << CompilerParser.T__31) | (1 << CompilerParser.T__32))) != 0):
                self.state = 286
                localctx._varType = self.varType()
                self.state = 287
                localctx._ID = self.match(CompilerParser.ID)
                localctx.s.append((localctx._varType.v, (None if localctx._ID is None else localctx._ID.text)))


            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CompilerParser.COMA:
                self.state = 292
                self.match(CompilerParser.COMA)
                self.state = 293
                localctx._varType = self.varType()
                self.state = 294
                localctx._ID = self.match(CompilerParser.ID)
                localctx.s.append((localctx._varType.v, (None if localctx._ID is None else localctx._ID.text)))
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            self.match(CompilerParser.T__1)
            localctx.v = localctx.s
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._varType = None # VarTypeContext

        def varType(self):
            return self.getTypedRuleContext(CompilerParser.VarTypeContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_funcReturnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncReturnType" ):
                listener.enterFuncReturnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncReturnType" ):
                listener.exitFuncReturnType(self)




    def funcReturnType(self):

        localctx = CompilerParser.FuncReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_funcReturnType)
        try:
            self.state = 310
            token = self._input.LA(1)
            if token in [CompilerParser.T__0, CompilerParser.T__31, CompilerParser.T__32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                localctx._varType = self.varType()
                localctx.v=localctx._varType.v

            elif token in [CompilerParser.T__30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(CompilerParser.T__30)
                localctx.v='void'

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self._functionalType = None # FunctionalTypeContext

        def functionalType(self):
            return self.getTypedRuleContext(CompilerParser.FunctionalTypeContext,0)


        def getRuleIndex(self):
            return CompilerParser.RULE_varType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarType" ):
                listener.enterVarType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarType" ):
                listener.exitVarType(self)




    def varType(self):

        localctx = CompilerParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_varType)
        try:
            self.state = 319
            token = self._input.LA(1)
            if token in [CompilerParser.T__31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(CompilerParser.T__31)
                localctx.v='int'

            elif token in [CompilerParser.T__32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 314
                self.match(CompilerParser.T__32)
                localctx.v='bool'

            elif token in [CompilerParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                localctx._functionalType = self.functionalType()
                localctx.v = localctx._functionalType.v

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionalTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.v = None
            self.s =  list()
            self._varType = None # VarTypeContext
            self._funcReturnType = None # FuncReturnTypeContext

        def funcReturnType(self):
            return self.getTypedRuleContext(CompilerParser.FuncReturnTypeContext,0)


        def varType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompilerParser.VarTypeContext)
            else:
                return self.getTypedRuleContext(CompilerParser.VarTypeContext,i)


        def getRuleIndex(self):
            return CompilerParser.RULE_functionalType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionalType" ):
                listener.enterFunctionalType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionalType" ):
                listener.exitFunctionalType(self)




    def functionalType(self):

        localctx = CompilerParser.FunctionalTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionalType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.match(CompilerParser.T__0)
            self.state = 327
            token = self._input.LA(1)
            if token in [CompilerParser.T__0, CompilerParser.T__31, CompilerParser.T__32]:
                self.state = 322
                localctx._varType = self.varType()
                localctx.s.append(localctx._varType.v)
                pass
            elif token in [CompilerParser.T__33]:
                self.state = 325
                self.match(CompilerParser.T__33)
                localctx.s.append('x')
                pass
            elif token in [CompilerParser.T__34, CompilerParser.COMA]:
                pass
            else:
                raise NoViableAltException(self)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CompilerParser.COMA:
                self.state = 329
                self.match(CompilerParser.COMA)
                self.state = 335
                token = self._input.LA(1)
                if token in [CompilerParser.T__0, CompilerParser.T__31, CompilerParser.T__32]:
                    self.state = 330
                    localctx._varType = self.varType()
                    localctx.s.append(localctx._varType.v)

                elif token in [CompilerParser.T__33]:
                    self.state = 333
                    self.match(CompilerParser.T__33)
                    localctx.s.append('x')

                else:
                    raise NoViableAltException(self)

                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 342
            self.match(CompilerParser.T__34)
            self.state = 343
            localctx._funcReturnType = self.funcReturnType()
            localctx.v = '(' + ','.join(localctx.s) + ')' + '->' + localctx._funcReturnType.v
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         




