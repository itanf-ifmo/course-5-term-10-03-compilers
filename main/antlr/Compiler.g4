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

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass
}

@parser::members {
def setContext(self, context):
    self.context = context

@staticmethod
def parse(source, context):
    lexer = CompilerLexer.CompilerLexer(antlr4.InputStream(source))
    lexer._listeners = [MyErrorListener(context)]
    stream = antlr4.CommonTokenStream(lexer)
    parser = CompilerParser(stream)
    parser._listeners = [MyErrorListener(context)]
    parser.setContext(context)

    bodies = parser.body().v

    for b in bodies:
        b.typecheck()

    return list(itertools.chain(*[i.resolve(context) for i in bodies if i is not None]))
}

expr returns [v]
    : t=BOOL {$v = BoolStatement(self.context, $t.text == 'true', ($t.line, $t.pos))}
    | INT {$v = ConstIntStatement(self.context, $INT.int, ($INT.line, $INT.pos))}
    | '(' e=expr ')' {$v=$e.v}
    | ID {$v = GetVariableStatement(self.context, $ID.text, ($ID.line, $ID.pos))}
    | <assoc=right> e=expr a=call_arguments {$v = FunctionExprCallStatement(self.context, $e.v, $a.v, $e.v._position).call_from_expression()}
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

func_expr_call returns [v]
    : e=expr a=call_arguments {$v = FunctionExprCallStatement(self.context, $e.v, $a.v, $e.v._position)}
    ;


call_arguments returns [v] locals [s = list()] :
    '('
        (expr {$s.append($expr.v)})?
        (',' expr {$s.append($expr.v)})*
    ')' {$v=$s};

variable_declaration_andassignment returns [v]
    : varType t=ID '=' expr {$v = DeclareAndAssignVariableStatement(self.context, $varType.v, $t.text, $expr.v, ($t.line, $t.pos))}
    ;

assignment returns [v]
    : ID t='=' expr {$v = AssignVariableStatement(self.context, $ID.text, $expr.v, ($t.line, $t.pos))}
    ;

write returns [v]
    : expr t='>>' {$v = PrintStatement(self.context, $expr.v, ($t.line, $t.pos))}
    | t='print' expr {$v = PrintStatement(self.context, $expr.v, ($t.line, $t.pos))}
    ;

read returns [v]
    : t='>>' ID {$v = ReadStatement(self.context, $ID.text, ($t.line, $t.pos))}
    | t='read' ID {$v = ReadStatement(self.context, $ID.text, ($t.line, $t.pos))}
    ;

seq returns [v]
    : assignment     {$v = $assignment.v}
    | write          {$v = $write.v}
    | read           {$v=$read.v}
    | scope          {$v = $scope.v}
    | if_expr        {$v = $if_expr.v}
    | while_expr     {$v = $while_expr.v}
    | func_expr_call {$v = $func_expr_call.v}
    | PASS           {$v = PassStatement(self.context, ($PASS.line, $PASS.pos))}
    | returnW        {$v = $returnW.v}
    ;

returnW returns [v]
    : t='return' e=expr {$v = ReturnStatement(self.context, $expr.v , ($t.line, $t.pos))}
    | t='return' {$v = ReturnStatement(self.context, None, ($t.line, $t.pos))}
    ;

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
    : variable_declaration {$v = $variable_declaration.v}
    | variable_declaration_andassignment {$v = $variable_declaration_andassignment.v}
    | function_declaration {$v = $function_declaration.v}
    ;

scope returns [v]
    : s='{' '}' {$v=ScopeStatement(self.context, [], ($s.line, $s.pos))}
    | s='{' {self.context.push('s', ($s.line, $s.pos))} body {$v = ScopeStatement(self.context, $body.v, ($s.line, $s.pos))} e='}' {self.context.pop(($e.line, $e.pos))};

variable_declaration returns [v]
    : t=varType ID {$v = DeclareVariableStatement(self.context, $t.v, $ID.text, ($ID.line, $ID.pos))}
    ;

function_declaration returns [v] :
    funcReturnType
    fn=ID
    function_parameters s='{'
        {self.context.push('f', ($s.line, $s.pos), $funcReturnType.v)}
            {self.context.push_func_params($function_parameters.v)}
            body
        {self.context.pop(($s.line, $s.pos))}
    '}'

    {$v = FunctionStatement(self.context, $funcReturnType.v, $fn.text, $function_parameters.v, $body.v, ($s.line, $s.pos))}
    ;

while_expr returns [v]
    : w='while' e=expr s=seq {$v = WhileStatement(self.context, $e.v, $s.v, ($w.line, $w.pos))}
    ;

if_expr returns [v]
    : i='if' e=expr t=seq 'else' f=seq {$v = IfStatement(self.context, $e.v, $t.v, $f.v, ($i.line, $i.pos))}
    | i='if' e=expr t=seq {$v = IfStatement(self.context, $e.v, $t.v, None, ($i.line, $i.pos))}
    ;

function_parameters returns [v] locals [s = list()] :
    '('
        (    varType ID {$s.append(($varType.v, $ID.text))})?
        (',' varType ID {$s.append(($varType.v, $ID.text))})*
    ')' {$v = $s};

funcReturnType returns [v]
    : varType  {$v=$varType.v}
    | 'void'   {$v='void'}
    ;

varType returns [v]
    : 'int' {$v='int'}
    | 'bool' {$v='bool'}
    | functionalType {$v = $functionalType.v}
    ;

functionalType returns [v] locals [s = list()]:
    '('
        (varType {$s.append($varType.v)} | 'X' {$s.append('x')}) ?
        (
            ',' (varType {$s.append($varType.v)} | 'X' {$s.append('x')})
        )*

    ')->' funcReturnType {$v = '(' + ','.join($s) + ')' + '->' + $funcReturnType.v}
    ;

BOOL
    : 'true'
    | 'false'
    ;

COMA : ',' ;
PASS : 'pass' ;

INT : DIGIT+ ;
ID : ALPHA (ALPHA | DIGIT | '_')* ;

COMMENT : '/*' .*? '*/' ->  channel(HIDDEN) ;
LINE_COMMENT : ('#' | '//') ~( '\r' | '\n' )* ->  channel(HIDDEN) ;
WS : [ \t\r\n]+ ->  channel(HIDDEN) ;

fragment ALPHA : [a-zA-Z] ;
fragment DIGIT : [0-9] ;

