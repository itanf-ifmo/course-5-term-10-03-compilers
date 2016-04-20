import os
from subprocess import Popen, PIPE
import unittest

from compiler.settings import *
from compiler import compiler, objects


def test(byte_code, stdin=None):
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    open(OUTPUT_FILE, 'wb').write(byte_code)
    p = Popen(["java", "A"], stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, cwd=OUTPUT_DIR)

    if stdin:
        p.stdin.write(stdin)

    o, e = p.communicate()
    return o.decode("utf-8").strip().replace('\n', ' '), e.decode("utf-8").strip(), p.returncode


# @unittest.skip("demonstrating skipping")
class TestBooleans(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_true(self):
        self.base('true >>', 'true')

    def test_false(self):
        self.base('false >>', 'false')

    def test_boolean_un_op_not1(self):
        self.base('!true >>', 'false')

    def test_boolean_un_op_not2(self):
        self.base('not true >>', 'false')

    def test_boolean_un_op_not3(self):
        self.base('! false >>', 'true')

    def test_boolean_un_op_not4(self):
        self.base('not false >>', 'true')

    def test_not_one(self):
        self.base('not 1 >>', 'false')

    def test_not_zero(self):
        self.base('! 0 >>', 'true')

    def test_not_not_one(self):
        self.base('! not 1 >>', 'true')

    def test_not_minus_one(self):
        self.base('! -1 >>', 'true')

    def test_minus_true(self):
        self.assertRaisesRegex(objects.CompileError, 'Unexpected unary operator for boolean expression: -', compiler, '- true >>')

    def test_true_or_true(self):
        self.base('true or true >>', 'true')

    def test_true_or_false(self):
        self.base('true or false >>', 'true')

    def test_false_or_true(self):
        self.base('false || true >>', 'true')

    def test_false_or_false(self):
        self.base('false or false >>', 'false')

    def test_false_or_one(self):
        self.base('false or 1 >>', 'true')

    def test_one_or_one(self):
        self.base('1 or 1 >>', 'true')

    def test_1234567890_or_1234567890(self):
        self.base('1234567890 or 1234567890 >>', 'true')

    def test_one_or_false(self):
        self.base('1 or false >>', 'true')

    def test_false_and_one(self):
        self.base('false and 1 >>', 'false')

    def test_one_and_false(self):
        self.base('1 && false >>', 'false')

    def test_one_and_true(self):
        self.base('1 && false >>', 'false')

    def test_not_not_true(self):
        self.base('!!true >>', 'true')

    def test_not_not_false(self):
        self.base('!!false >>', 'false')

    def test_1234567890_and_1234567890(self):
        self.base('1234567890 and 1234567890 >>', 'true')

    def test_1234567890_and_1234567891(self):
        self.base('1234567890 and 1234567891 >>', 'true')

    def test_not_true_or_false(self):
        self.base('not true or false >>', 'false')

    def test_not__true_and_false(self):
        self.base('not ( true and false ) >>', 'true')

    def test_not_true_and_false(self):
        self.base('not true and false >>', 'false')

    def test_true_or_false_and_false(self):
        self.base('true or false and true >>', 'true')

    def test_true_plus_true(self):
        self.assertRaisesRegex(objects.CompileError, 'Unexpected operator for boolean parameters: +', compiler, 'true + true >>')


class TestBasics(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_empty(self):
        self.base('', '')


class TestNumbers(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_one(self):
        self.base('1 >>', '1')

    def test_1123333333(self):
        self.base('1123333333 >>', '1123333333')

    def test_minus_one(self):
        self.base('-1 >>', '-1')

    def test_one_plus_two(self):
        self.base('1 + 2 >>', '3')

    def test_one_plus_zero(self):
        self.base('1 + 0 >>', '1')

    def test_one_plus_1123333333(self):
        self.base('1 + 1123333333 >>', '1123333334')

    def test_one_plus_minus_two(self):
        self.base('1 + -2 >>', '-1')

    def test_one_minus_two(self):
        self.base('1 - 2 >>', '-1')

    def test_one_minus_minus_two(self):
        self.base('1 - -2 >>', '3')

    def test_one_minus_two_plus_three(self):
        self.base('1 - 2 + 3 >>', '2')

    def test_one_minus__two_plus_three(self):
        self.base('1 - (2 + 3) >>', '-4')

    def test_two_multiply_three(self):
        self.base('2 * 3 >>', '6')

    def test_one_minus_two_multiply_three(self):
        self.base('1 - 2 * 3 >>', '-5')

    def test__one_minus_two__multiply_three(self):
        self.base('(1 - 2) * 3 >>', '-3')

    def test_one_multiply_three_minus_minus_tow_multiply_three(self):
        self.base('1 * 3 - -2 * 3 >>', '9')

    def test_minus_one_multiply_minus_five(self):
        self.base('-1 * -5 >>', '5')

    def test_one_divide_two(self):
        self.base('1 / 2 >>', '0')

    def test_one_remainder_two(self):
        self.base('1 % 2 >>', '1')

    def test_two_divide_two(self):
        self.base('2 / 2 >>', '1')

    def test_two_remainder_two(self):
        self.base('2 % 2 >>', '0')

    def test_three_divide_two(self):
        self.base('3 / 2 >>', '1')

    def test_three_remainder_two(self):
        self.base('3 % 2 >>', '1')


class TestComparison(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual(expected_output, stdout)

    def test_one_lt_two(self):
        self.base('1 < 2 >>', 'true')

    def test_one_le_two(self):
        self.base('1 <= 2 >>', 'true')

    def test_one_gt_two(self):
        self.base('1 > 2 >>', 'false')

    def test_one_ge_two(self):
        self.base('1 >= 2 >>', 'false')

    def test_one_ne_two(self):
        self.base('1 != 2 >>', 'true')

    def test_one_eq_two(self):
        self.base('1 == 2 >>', 'false')

    def test_two_eq_two(self):
        self.base('2 == 2 >>', 'true')

    def test_two_ne_two(self):
        self.base('2 != 2 >>', 'false')

    def test_true_eq_true(self):
        self.base('true == true >>', 'true')

    def test_true_eq_false(self):
        self.base('true == false >>', 'false')

    def test_two_lt_two(self):
        self.base('2 < 2 >>', 'false')

    def test_two_le_two(self):
        self.base('2 <= 2 >>', 'true')

    def test_true_le_two(self):
        self.assertRaisesRegex(objects.CompileError, 'Type of operand mismatches: bool <= int', compiler, 'true <= 2 >>')

    def test_true_le_true(self):
        self.base('true <= true >>', 'true')

    def test_false_lt_true(self):
        self.base('false <= true >>', 'true')


class TestVariables(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_int_a(self):
        self.base('int a', '')

    def test_already_defined(self):
        self.assertRaisesRegex(objects.CompileError, 'Variable a already defined', compiler, 'int a; int a;')

    def test_int_a__int_b(self):
        self.base('int a;int b;', '')

    def test_int_a__one(self):
        self.base('int a; a = 1', '')

    def test_int_aa3dfD22_3132313sfc(self):
        self.base('int aa3dfD22_3132313sfc = 1; aa3dfD22_3132313sfc>>', '1')

    # def test_use_before_declare(self):
    #     self.base('a = 1; int a; a>>', '1')

    def test_declare_and_define(self):
        self.base('int a = 1; a>>', '1')

    def test_declare_define_and_redefine(self):
        self.base('int a = 1; a>>; a = 2; a>>', '1 2')

    def test_int_a__one__print(self):
        self.base('int a; a = 1; a>>', '1')

    def test_one__int_a__print(self):
        self.assertRaisesRegex(objects.CompileError, 'Variable a is not defined', compiler, 'a = 1')

    def test_reassign(self):
        self.base('int a; a = 1; a>>; a = 2; a>>', '1 2')

    def test_sum_vars(self):
        self.base('int a; a = 1; int b; b = 2; a + b>>', '3')

    def test_bool_var(self):
        self.base('bool a; a = true; a>>', 'true')

    def test_bool_var_number_expr(self):
        msg = "Type bool of variable a doesn't matches expression type int"
        self.assertRaisesRegex(objects.CompileError, msg, compiler, 'bool a; a = 1')

    def test_complex(self):
        self.base('int b; int a; a = 1 + 2; b = 2; int c; c = a * a / b; c >>', '4')

    def test_complex2(self):
        self.base('int b = 10; int a = 1 + 2; b = 3; int c = a * a % b; c >>', '0')


class TestScope(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_empty(self):
        self.base('{}', '')

    def test_simple(self):
        self.base('{1>>}', '1')

    def test_var_in_scope(self):
        self.base('{int a = 0; a>>}', '0')

    def test_var_out_scope(self):
        self.base('int a = 1; a>>; {a>>}; a>>', '1 1 1')

    def test_use_var_out_of_scope(self):
        self.assertRaisesRegex(objects.CompileError, 'Variable a is not defined', compiler, '{int a = 0; a>>}; a>>')

    def test_already_defined_in_scope(self):
        self.assertRaisesRegex(objects.CompileError, 'Variable a already defined', compiler, '{int a; int a}')

    def test_overriding_variable(self):
        self.base('int a = 1; a>>; {int a = 0; a>>}; a>>', '1 0 1')

    def test_assign_global_variable(self):
        self.base('int a = 1; a>>; {a = 0; a>>}; a>>', '1 0 0')


class TestIfCondition(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_empty_true_short(self):
        self.base('if true {}', '')

    def test_empty_false_short(self):
        self.base('if false {}', '')

    def test_empty_true(self):
        self.base('if true {} else {}', '')

    def test_empty_false(self):
        self.base('if false {} else {}', '')

    def test_true_short(self):
        self.base('if true 1 >>', '1')

    def test_false_short(self):
        self.base('if false 1 >>', '')

    def test_true(self):
        self.base('if true 1 >> else 2 >>', '1')

    def test_false(self):
        self.base('if false 1 >> else 2 >>', '2')

    def test_not_true(self):
        self.base('if not true 1 >> else 2 >>', '2')

    def test_not_false(self):
        self.base('if ! false 1 >> else 2 >>', '1')

    def test_not_not_true(self):
        self.base('if !! true 1 >> else 2 >>', '1')

    def test_not_not_false(self):
        self.base('if not not false 1 >> else 2 >>', '2')

    def test_zero(self):
        self.base('if 0 true >> else false >>', 'false')

    def test_one(self):
        self.base('if 1 true >> else false >>', 'true')

    def test_declare_var_in_condition(self):
        self.assertRaisesRegex(objects.ParseError, 'no viable alternative at input', compiler, 'if false int a = 1')

    def test_set_var_in_if(self):
        self.base('int a = 1; a>>; if a - 1 {a = 4; 1>>} else {a = 3; 2>>}; a>>', '1 2 3')

    def test_declare_and_use_var_in_condition(self):
        self.base('int a = 1; a>>; if a - 1 {int a = 4; a>>} else {int a = 3; a>>}; a>>', '1 3 1')


class TestWhile(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_false(self):
        self.base('while false { 1 >> }; 2 >>', '2')

    def test_once(self):
        self.base('bool a = true; a>>; while a { 1 >>; a = false}; a>>', 'true 1 false')

    def test_many_times(self):
        self.base('int a = 10; while a { a = a - 1; a >> }; -1 >>', '9 8 7 6 5 4 3 2 1 0 -1')


class TestFunctions(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_false(self):
        self.base('void main(int a) {1>>} ; main(1, !!1)', '1')

    # def test_once(self):
    #     self.base('bool a = true; a>>; while a { 1 >>; a = false}; a>>', 'true 1 false')
    #
    # def test_many_times(self):
    #     self.base('int a = 10; while a { a = a - 1; a >> }; -1 >>', '9 8 7 6 5 4 3 2 1 0 -1')


if __name__ == '__main__':
    unittest.main()
