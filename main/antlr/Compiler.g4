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
        pass
#        raise Exception("Oh no1!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass
#        raise ParseError(self._context, 0, 0, str((recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs)))
#        raise Exception("Oh no2!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass
#        raise Exception("Oh no3!!")
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
    return list(itertools.chain(*[i.resolve(context) for i in parser.body().v]))
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

variable_declaration_andassignment returns [v] : TYPE t=ID '=' expr {$v = DeclareAndAssignVariableStatement(self.context, $TYPE.text, $t.text, $expr.v, ($t.line, $t.pos))} ;

assignment returns [v] : ID t='=' expr {$v = AssignVariableStatement(self.context, $ID.text, $expr.v, ($t.line, $t.pos))} ;

write returns [v]: expr t='>>' {$v = PrintStatement(self.context, $expr.v, ($t.line, $t.pos))};
read : '>>' ID ;

//write : 'print ' expr {print('print ', $expr.v)};
//read : 'read' ID ;

seq returns [v]
    : assignment {$v=$assignment.v}
    | write {$v=$write.v}
    | read
    | scope {$v=$scope.v}
    | if_expr {$v=$if_expr.v}
    | while_expr
    | func_call
    | PASS
    | returnW
    ;

//body : (seq (';' seq)*)? ;

body returns [v] locals [s = list()] : (
  body_seq {$s.append($body_seq.v)}
  (';' body_seq {$s.append($body_seq.v)})*
  ';'?
)? {$v=$s};

body_seq returns [v]
    : declarations {$v = $declarations.v}
    | seq {$v = $seq.v}
    ;

declarations returns [v]
    : variable_declaration {$v=$variable_declaration.v}
    | variable_declaration_andassignment {$v=$variable_declaration_andassignment.v}
    | function_declaration
    ;

scope returns [v]
    : s='{' '}' {$v=ScopeStatement(self.context, [], ($s.line, $s.pos))}
    | s='{' {self.context.push(($s.line, $s.pos))} body {$v=ScopeStatement(self.context, $body.v, ($s.line, $s.pos))} e='}' {self.context.pop(($e.line, $e.pos))};

// ((';' | WS) y=seq {$s.append($y.text); $r = $s})+


variable_declaration returns [v]: t=TYPE ID {$v = DeclareVariableStatement(self.context, $t.text, $ID.text, ($ID.line, $ID.pos))};
function_declaration : function_type function_name '(' function_parameters? ')' '{' body '}'
    {self.functions.append(Function($function_type.text, $function_name.text, $function_parameters.text, $body.v)) } ;

returnW: 'return' expr? ;

while_expr : 'while' expr '{' body '}' ;
if_expr returns [v]
    : i='if' e=expr t=seq 'else' f=seq {$v = IfStatement(self.context, $e.v, $t.v, $f.v, ($i.line, $i.pos))}
    | i='if' e=expr t=seq {$v = IfStatement(self.context, $e.v, $t.v, None, ($i.line, $i.pos))}
    ;


function_type : TYPE | 'void' ;
function_name : ID ;
function_parameters : (TYPE ID ',')* TYPE ID ;

TYPE : 'int' | 'bool' ;
BOOL : 'true' | 'false' ;

COMA : ',' ;
PASS : 'pass' ;

INT : DIGIT+ ;
ID : ALPHA (ALPHA | DIGIT | '_')* ;
//COMMENT : '/*' .*? '*/' -> skip ;
//WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

COMMENT : '/*' .*? '*/' ->  channel(HIDDEN) ;
WS : [ \t\r\n]+ ->  channel(HIDDEN) ;

fragment ALPHA : [a-zA-Z] ;
fragment DIGIT : [0-9] ;

