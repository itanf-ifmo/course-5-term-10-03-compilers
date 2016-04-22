# Generated from ./antlr/Compiler.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CompilerParser import CompilerParser
else:
    from CompilerParser import CompilerParser

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


# This class defines a complete listener for a parse tree produced by CompilerParser.
class CompilerListener(ParseTreeListener):

    # Enter a parse tree produced by CompilerParser#expr.
    def enterExpr(self, ctx:CompilerParser.ExprContext):
        pass

    # Exit a parse tree produced by CompilerParser#expr.
    def exitExpr(self, ctx:CompilerParser.ExprContext):
        pass


    # Enter a parse tree produced by CompilerParser#func_call.
    def enterFunc_call(self, ctx:CompilerParser.Func_callContext):
        pass

    # Exit a parse tree produced by CompilerParser#func_call.
    def exitFunc_call(self, ctx:CompilerParser.Func_callContext):
        pass


    # Enter a parse tree produced by CompilerParser#func_expr_call.
    def enterFunc_expr_call(self, ctx:CompilerParser.Func_expr_callContext):
        pass

    # Exit a parse tree produced by CompilerParser#func_expr_call.
    def exitFunc_expr_call(self, ctx:CompilerParser.Func_expr_callContext):
        pass


    # Enter a parse tree produced by CompilerParser#call_arguments.
    def enterCall_arguments(self, ctx:CompilerParser.Call_argumentsContext):
        pass

    # Exit a parse tree produced by CompilerParser#call_arguments.
    def exitCall_arguments(self, ctx:CompilerParser.Call_argumentsContext):
        pass


    # Enter a parse tree produced by CompilerParser#variable_declaration_andassignment.
    def enterVariable_declaration_andassignment(self, ctx:CompilerParser.Variable_declaration_andassignmentContext):
        pass

    # Exit a parse tree produced by CompilerParser#variable_declaration_andassignment.
    def exitVariable_declaration_andassignment(self, ctx:CompilerParser.Variable_declaration_andassignmentContext):
        pass


    # Enter a parse tree produced by CompilerParser#assignment.
    def enterAssignment(self, ctx:CompilerParser.AssignmentContext):
        pass

    # Exit a parse tree produced by CompilerParser#assignment.
    def exitAssignment(self, ctx:CompilerParser.AssignmentContext):
        pass


    # Enter a parse tree produced by CompilerParser#write.
    def enterWrite(self, ctx:CompilerParser.WriteContext):
        pass

    # Exit a parse tree produced by CompilerParser#write.
    def exitWrite(self, ctx:CompilerParser.WriteContext):
        pass


    # Enter a parse tree produced by CompilerParser#read.
    def enterRead(self, ctx:CompilerParser.ReadContext):
        pass

    # Exit a parse tree produced by CompilerParser#read.
    def exitRead(self, ctx:CompilerParser.ReadContext):
        pass


    # Enter a parse tree produced by CompilerParser#seq.
    def enterSeq(self, ctx:CompilerParser.SeqContext):
        pass

    # Exit a parse tree produced by CompilerParser#seq.
    def exitSeq(self, ctx:CompilerParser.SeqContext):
        pass


    # Enter a parse tree produced by CompilerParser#returnW.
    def enterReturnW(self, ctx:CompilerParser.ReturnWContext):
        pass

    # Exit a parse tree produced by CompilerParser#returnW.
    def exitReturnW(self, ctx:CompilerParser.ReturnWContext):
        pass


    # Enter a parse tree produced by CompilerParser#body.
    def enterBody(self, ctx:CompilerParser.BodyContext):
        pass

    # Exit a parse tree produced by CompilerParser#body.
    def exitBody(self, ctx:CompilerParser.BodyContext):
        pass


    # Enter a parse tree produced by CompilerParser#body_seq.
    def enterBody_seq(self, ctx:CompilerParser.Body_seqContext):
        pass

    # Exit a parse tree produced by CompilerParser#body_seq.
    def exitBody_seq(self, ctx:CompilerParser.Body_seqContext):
        pass


    # Enter a parse tree produced by CompilerParser#declarations.
    def enterDeclarations(self, ctx:CompilerParser.DeclarationsContext):
        pass

    # Exit a parse tree produced by CompilerParser#declarations.
    def exitDeclarations(self, ctx:CompilerParser.DeclarationsContext):
        pass


    # Enter a parse tree produced by CompilerParser#scope.
    def enterScope(self, ctx:CompilerParser.ScopeContext):
        pass

    # Exit a parse tree produced by CompilerParser#scope.
    def exitScope(self, ctx:CompilerParser.ScopeContext):
        pass


    # Enter a parse tree produced by CompilerParser#variable_declaration.
    def enterVariable_declaration(self, ctx:CompilerParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by CompilerParser#variable_declaration.
    def exitVariable_declaration(self, ctx:CompilerParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by CompilerParser#function_declaration.
    def enterFunction_declaration(self, ctx:CompilerParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by CompilerParser#function_declaration.
    def exitFunction_declaration(self, ctx:CompilerParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by CompilerParser#while_expr.
    def enterWhile_expr(self, ctx:CompilerParser.While_exprContext):
        pass

    # Exit a parse tree produced by CompilerParser#while_expr.
    def exitWhile_expr(self, ctx:CompilerParser.While_exprContext):
        pass


    # Enter a parse tree produced by CompilerParser#if_expr.
    def enterIf_expr(self, ctx:CompilerParser.If_exprContext):
        pass

    # Exit a parse tree produced by CompilerParser#if_expr.
    def exitIf_expr(self, ctx:CompilerParser.If_exprContext):
        pass


    # Enter a parse tree produced by CompilerParser#function_parameters.
    def enterFunction_parameters(self, ctx:CompilerParser.Function_parametersContext):
        pass

    # Exit a parse tree produced by CompilerParser#function_parameters.
    def exitFunction_parameters(self, ctx:CompilerParser.Function_parametersContext):
        pass


    # Enter a parse tree produced by CompilerParser#funcReturnType.
    def enterFuncReturnType(self, ctx:CompilerParser.FuncReturnTypeContext):
        pass

    # Exit a parse tree produced by CompilerParser#funcReturnType.
    def exitFuncReturnType(self, ctx:CompilerParser.FuncReturnTypeContext):
        pass


    # Enter a parse tree produced by CompilerParser#varType.
    def enterVarType(self, ctx:CompilerParser.VarTypeContext):
        pass

    # Exit a parse tree produced by CompilerParser#varType.
    def exitVarType(self, ctx:CompilerParser.VarTypeContext):
        pass


    # Enter a parse tree produced by CompilerParser#functionalType.
    def enterFunctionalType(self, ctx:CompilerParser.FunctionalTypeContext):
        pass

    # Exit a parse tree produced by CompilerParser#functionalType.
    def exitFunctionalType(self, ctx:CompilerParser.FunctionalTypeContext):
        pass


