grammar Compiler;

options {
    language=Python3;
}

@parser::header {
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
        raise Exception("Oh no!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise Exception("Oh no!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Oh no!!")
}

@parser::members {
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
    return list(itertools.chain(*[i.resolve(context) for i in parser.body().r]))
}

expr returns [v]
    : t=BOOL {$v = BoolStatement(self.context, $t.text == 'true', ($t.line, $t.pos))}
    | INT {$v = ConstIntStatement(self.context, $INT.int, ($INT.line, $INT.pos))}
    | func_call {$v = ('call', $func_call.text)}
    | '(' e=expr ')' {$v=$e.v}
    | ID {$v = GetVariableStatement(self.context, $ID.text, ($ID.line, $ID.pos))}

    // operators:
    |         o='-'                e =expr {$v = UnaryOperatorStatement(self.context, $o.text, $e.v, ($o.line, $o.pos))}
    | e1=expr o=('*'  | '/' | '%') e2=expr {$v = OperatorStatement(self.context, $e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('+'  | '-')       e2=expr {$v = OperatorStatement(self.context, $e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('<'  | '<='
                |'>'  | '>=')      e2=expr {$v = OperatorStatement(self.context, $e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('==' | '!=')      e2=expr {$v = OperatorStatement(self.context, $e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    |         o=('!'  | 'not')     e =expr {$v = UnaryOperatorStatement(self.context, $o.text, $e.v, ($o.line, $o.pos))}
    | e1=expr o=('&&' | 'and')     e2=expr {$v = OperatorStatement(self.context, $e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('||' | 'or')      e2=expr {$v = OperatorStatement(self.context, $e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    ;

func_call returns [v] : ID '(' ( (expr ',' )* expr )? ')' {print('avaliableFs: ', $ID.pos)};

variable_declaration_andassignment returns [v] : TYPE t=ID '=' expr {$v = DeclareAndAssigneVariableStatement(self.context, $TYPE.text, $t.text, $expr.v, ($t.line, $t.pos))} ;

assignment returns [v] : ID t='=' expr {$v = AssignVariableStatement(self.context, $ID.text, $expr.v, ($t.line, $t.pos))} ;

write returns [v]: expr t='>>' {$v = PrintStatement(self.context, $expr.v, ($t.line, $t.pos))};
read : '>>' ID ;

//write : 'print ' expr {print('print ', $expr.v)};
//read : 'read' ID ;

seq returns [v]
    : variable_declaration {$v=$variable_declaration.v}
    | variable_declaration_andassignment {$v=$variable_declaration_andassignment.v}
    | assignment {$v=$assignment.v}
    | write {$v=$write.v}
    | read
    | if_expr
    | while_expr
    | func_call
    | PASS
    | returnW
    | function_declaration
    ;

//body : (seq (';' seq)*)? ;

body returns [r] locals [s = list()] : (
  t=seq {$s.append($seq.v)}
  (';' seq {$s.append($seq.v)})*
  ';'?
)? {$r=$s};


// ((';' | WS) y=seq {$s.append($y.text); $r = $s})+


variable_declaration returns [v]: t=TYPE ID {$v = DeclareVariableStatement(self.context, $t.text, $ID.text, ($ID.line, $ID.pos))};
function_declaration : function_type function_name '(' function_parameters? ')' '{' body '}'
    {self.functions.append(Function($function_type.text, $function_name.text, $function_parameters.text, $body.r)) } ;

returnW: 'return' expr? ;

while_expr : 'while' expr ':' '{' body '}' ;
if_expr : 'if' expr ':' '{' body '}' ( 'else' '{' body '}' )? ;


function_type : TYPE | 'void' ;
function_name : ID ;
function_parameters : (TYPE ID ',')* TYPE ID ;

TYPE : 'int' | 'bool' ;
BOOL : 'true' | 'false' ;

COMA : ',' ;
PASS : 'pass' ;

INT : DIGIT+ ;
ID : ALPHA (ALPHA | DIGIT)* ;
//COMMENT : '/*' .*? '*/' -> skip ;
//WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

COMMENT : '/*' .*? '*/' ->  channel(HIDDEN) ;
WS : [ \t\r\n]+ ->  channel(HIDDEN) ;

fragment ALPHA : [a-zA-Z] ;
fragment DIGIT : [0-9] ;

