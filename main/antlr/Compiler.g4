grammar Compiler;

options {
    language=Python3;
}

@parser::header {
from compiler.objects import *
}

@parser::init {
self.functions = []
}
@parser::members {
}

expr returns [v]
    : t=BOOL {$v = BoolStatement($t.text == 'true', ($t.line, $t.pos))}
    | INT {$v = ConstIntStatement($INT.int, ($t.line, $t.pos))}
    | func_call {$v = ('call', $func_call.text)}
    | '(' e=expr ')' {$v=$e.v}
    | ID {$v = ('var', $ID.text)}

    // operators:
    |         o='-'                e =expr {$v = UnaryOperatorStatement($o.text, $e.v, ($o.line, $o.pos))}
    | e1=expr o=('*'  | '/' | '%') e2=expr {$v = OperatorStatement($e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('+'  | '-')       e2=expr {$v = OperatorStatement($e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('<'  | '<='
                |'>'  | '>=')      e2=expr {$v = OperatorStatement($e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('==' | '!=')      e2=expr {$v = OperatorStatement($e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    |         o=('!'  | 'not')     e =expr {$v = UnaryOperatorStatement($o.text, $e.v, ($o.line, $o.pos))}
    | e1=expr o=('&&' | 'and')     e2=expr {$v = OperatorStatement($e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    | e1=expr o=('||' | 'or')      e2=expr {$v = OperatorStatement($e1.v, $o.text, $e2.v, ($o.line, $o.pos))}
    ;

func_call : ID '(' ( (expr ',' )* expr )? ')' {print('avaliableFs: ', $ID.pos)};

assignment : ID '=' expr {print($ID.text, $expr.text, self.a)} ;
root_assignment : ID '=' expr {print($ID.text, $expr.text, self.a)} ;

write returns [v]: expr t='>>' {$v = PrintStatement($expr.v, ($t.line, $t.pos))};
read : '>>' ID ;

//write : 'print ' expr {print('print ', $expr.v)};
//read : 'read' ID ;

seq returns [v]
    :
    assignment
    | t=write {$v=$t.v}
    | read
    | if_expr
    | while_expr
    | func_call
    | variable_declaration
    | PASS
    | returnW
    | variable_declaration
    | function_declaration
    ;

//body : (seq (';' seq)*)? ;

body returns [r] locals [s = list()] : (
  t=seq {$s.append($seq.v)}
  (';' seq {$s.append($seq.v)})*
  ';'?
)? {$r=$s};


// ((';' | WS) y=seq {$s.append($y.text); $r = $s})+


variable_declaration : TYPE ID ;
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

