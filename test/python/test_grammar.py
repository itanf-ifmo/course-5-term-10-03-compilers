import os
from subprocess import Popen, PIPE
import unittest

from compiler.settings import *
from compiler import _compiler, objects, build


def test(byte_code, stdin=None):
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    with open(OUTPUT_FILE, 'wb') as output_file:
        output_file.write(byte_code)

    p = Popen(["java", "A"], stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, cwd=OUTPUT_DIR)

    if stdin:
        p.stdin.write(stdin.encode())

    o, e = p.communicate()
    return o.decode("utf-8").strip().replace('\n', ' '), e.decode("utf-8").strip(), p.returncode


# @unittest.skip("demonstrating skipping")
class TestBooleans(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
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
        self.assertRaisesRegex(objects.CompileError, 'Unexpected unary operator for boolean expression: -', _compiler, '- true >>')

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
        self.assertRaisesRegex(objects.CompileError, 'Unexpected operator for boolean parameters: +', _compiler, 'true + true >>')


class TestBasics(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_empty(self):
        self.base('', '')

    def test_pass(self):
        self.base('pass', '')

    def test_pass_in_if(self):
        self.base('if true pass else pass', '')


class TestNumbers(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
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
        stdout, stderr, rc = test(_compiler(src))
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
        self.assertRaisesRegex(objects.CompileError, 'Type of operand mismatches: bool <= int', _compiler, 'true <= 2 >>')

    def test_true_le_true(self):
        self.base('true <= true >>', 'true')

    def test_false_lt_true(self):
        self.base('false <= true >>', 'true')


class TestVariables(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_int_a(self):
        self.base('int a', '')

    def test_already_defined(self):
        self.assertRaisesRegex(objects.CompileError, 'Variable a already defined', _compiler, 'int a; int a;')

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
        self.assertRaisesRegex(objects.CompileError, 'Variable a is not defined', _compiler, 'a = 1')

    def test_reassign(self):
        self.base('int a; a = 1; a>>; a = 2; a>>', '1 2')

    def test_sum_vars(self):
        self.base('int a; a = 1; int b; b = 2; a + b>>', '3')

    def test_bool_var(self):
        self.base('bool a; a = true; a>>', 'true')

    def test_bool_var_number_expr(self):
        msg = "Type bool of variable a doesn't matches expression type int"
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, 'bool a; a = 1')

    def test_complex(self):
        self.base('int b; int a; a = 1 + 2; b = 2; int c; c = a * a / b; c >>', '4')

    def test_complex2(self):
        self.base('int b = 10; int a = 1 + 2; b = 3; int c = a * a % b; c >>', '0')

    def test_complex3(self):
        self.base('''

        int a = 1;
        int b = 2;

        a + b >>;
        {
            int c = 4;
            int d = 5;

            a + b >>;
            a + b + c + d >>;

            {
                int e = 7;
                int g = 8;
                int f = 9;

                a + b >>;
                a + b + c + d >>;
                a + b + c + d + e + f + g >>;
            };

            a + b + c + d >>;
        };

        a + b >>;
        ''', '3 3 12 3 12 36 12 3')


class TestScope(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
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
        msg = 'Variable\(or function\) a is not defined'
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, '{int a = 0; a>>}; a>>')

    def test_already_defined_in_scope(self):
        self.assertRaisesRegex(objects.CompileError, 'Variable a already defined', _compiler, '{int a; int a}')

    def test_overriding_variable(self):
        self.base('int a = 1; a>>; {int a = 0; a>>}; a>>', '1 0 1')

    def test_assign_global_variable(self):
        self.base('int a = 1; a>>; {a = 0; a>>}; a>>', '1 0 0')


class TestIfCondition(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
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
        self.assertRaisesRegex(objects.ParseError, 'no viable alternative at input', _compiler, 'if false int a = 1')

    def test_set_var_in_if(self):
        self.base('int a = 1; a>>; if a - 1 {a = 4; 1>>} else {a = 3; 2>>}; a>>', '1 2 3')

    def test_declare_and_use_var_in_condition(self):
        self.base('int a = 1; a>>; if a - 1 {int a = 4; a>>} else {int a = 3; a>>}; a>>', '1 3 1')


class TestWhile(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_false(self):
        self.base('while false { 1 >> }; 2 >>', '2')

    def test_once(self):
        self.base('bool a = true; a>>; while a { 1 >>; a = false}; a>>', 'true 1 false')

    def test_many_times(self):
        self.base('int a = 10; while a { a = a - 1; a >> }; -1 >>', '9 8 7 6 5 4 3 2 1 0 -1')


class TestComments(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_block(self):
        self.base('''
        1>>;
        /*
        2>>;
        3>>;
        */
        4>>;
        ''', '1 4')

    def test_line_slashes(self):
        self.base('''
        1>>;
        // 2>>;
        3>>;
        // 4>>;
        ''', '1 3')

    def test_line_sharp(self):
        self.base('''
        # 1>>;
        2>>;
        # 3>>;
        4>>;
        ''', '2 4')

    def test_at_the_end_of_instruction(self):
        self.base('''
        1>>; # 2>>;
        3>>; // 4>>;
        ''', '1 3')

    def test_inline(self):
        self.base('''
        1 + 2 /* *4 */ >>
        ''', '3')


class TestFunctions(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_empty_function(self):
        self.base('void a() {} ; a();', '')

    def test_once(self):
        self.base('void a() {1>>} ; a();', '1')

    def test_double_call(self):
        self.base('int a() {1>>} ; a(); a();', '1 1')

    def test_two_functions(self):
        self.base('void a() {1>>}; int b() {2>>} ; a(); b();', '1 2')

    def test_function_not_defined(self):
        msg = 'Variable\(or function\) a is not defined'
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, 'a();')

    def test_tow_function_reverse_order(self):
        self.base('void a() {1>>}; int b() {2>>}; b(); a();', '2 1')

    def test_more_functions(self):
        self.base('void a() {1>>}; int b() {2>>}; bool c() {3>>}; a() ; b() ; c();', '1 2 3')

    # def test_overloading(self):  # temporary disabled
    #     self.base('void a() {1>>}; int a(int c) {2>>}; a() ; a(1)', '1 2')

    def test_duplicate(self):
        msg = 'Error: function\(or variable\) with name a already defined'
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, 'void a() {}; int a() {}')

    # def test_same_name_as_variable(self):  # temporary disabled
    #     self.base('int a = 0; void a(){ a >> }; a(); a = a + 1; a>>', '0 1')

    def test_scope_var(self):
        self.base('void f() { int a }; int a', '')

    def test_do_not_override_globals(self):
        self.base('void f() { int a = 2; int b = 3; a>>; b>> }; int a2 = 0; a2>>; f(); a2 >>', '0 2 3 0')

    def test_call_from_function_1(self):
        self.base('''
        void g() {
            int a = 4;
            int b = 5;
            a>>;
            b>>
        };

        int a2 = 0;
        void f() {
            int a = 2;
            int b = 3;
            a>>;

            g();

            b>>;
            a2>>;
            a2 = a2 + 1
        };

        a2>>;
        f();
        a2>>
        ''', '0 2 4 5 3 0 1')

    def test_call_from_function_2(self):
        self.base('''
        void g() {
            int a = 4;
            int b = 5;
            a>>;                  // 5
            b>>;                  // 6
        };

        int a2 = 0;
        void f() {
            int a = 2;
            int b = 3;
            a>>;                  // 13
            {
                int a = -1;
                int c = 8;
                int d = 9;


                c + d + a >> ;
                g();

                c + d + a >> ;
            };

            b>>;
            a2>>;
            a2 = a2 + 1
        };

        a2>>;
        f();
        a2>>
        ''', '0 2 16 4 5 16 3 0 1')

    def test_call_function_from_function(self):
        self.base('void f(){ 1>> }; void g(){ f(); }; g();', '1')

    def test_two_params(self):
        self.base('''
        void a(int c, bool v) {
          if v c>>
        };

        a(1, false);
        a(2, true);
        ''', '2')

    def test_check_signatures(self):
        msg = 'Error: Mismatch signatures of called function: expected \(int,bool\)\-\>void but was \(int,int\)\-\>\?'
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, 'void a(int c, bool v) { }; a(1, 1); ')

    def test_param_name_are_same(self):
        self.base('void a(int a) {a >>}; a(1);', '1')

    def test_return_void(self):
        self.base('''
        void a() {
          return;
          1>>
        };

        a();
        ''', '')

    def test_type_check_return(self):
        msg = 'Error: This function should return void but found int'
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, 'void a() { return 1 }')

    def test_void_in_expr(self):
        msg = 'Error: could not print void at'
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, 'void a() { }; a() >>')

    def test_wrong_type_in_expr(self):
        msg = 'Error: Type of operand mismatches: bool \+ int'
        self.assertRaisesRegex(objects.CompileError, msg, _compiler, 'bool a() { }; a() + 1 >>')

    def test_return_to_expr(self):
        self.base('int a() { return 3 }; a() + 1 >>', '4')

    def test_return_default_int(self):
        self.base('int a() { true>> }; a() >>', 'true 0')

    def test_return_default_bool(self):
        self.base('bool a() { 1>> }; a() >>', '1 false')

    def test_bug_ret_from_if(self):
        self.base('''
        int h(int b) {
          if b == 1
            return 1
        };

        h(1) >>;
        h(-1) >>;
        ''', '1 0')

    def test_recursion(self):
        self.base('''
        int fact(int a) {
          if a <= 1
            return 1;

          return a * fact(a - 1);
        };

        fact(5) >>;
        fact(1) >>;
        ''', '120 1')


class TestHigherOrderFunctions(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr, rc = test(_compiler(src))
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_func_var(self):
        self.base('''
        void f() { 1>> };
        f();
        ()->void a = f;
        a();
        ''', '1 1')

    def test_reuse_function_var(self):
        self.base('''
        void f() { 1>> };
        void g() { 2>> };

        ()->void a = f;
        a();

        a = g;

        a();
        a = f;
        a();
        g();
        ''', '1 2 1 2')

    def test_if(self):
        self.base('''
        void f() { 1>> };
        void g() { 2>> };

        ()->void a;

        if 1 + 2 >= 3 {
          a = f;
        } else {
          a = g;
        };

        a();
        ''', '1')

    def test_if2(self):
        self.base('''
        void f() { 1>> };
        void g() { 2>> };

        ()->void a;

        if 1 + 2 < 3 {
          a = f;
        } else {
          a = g;
        };

        a();
        ''', '2')

    def test_as_param(self):
        self.base('''
        int q = 4;
        void f(int a, int v) { q + a + 1>>; v >> };
        void g(int b, int v) { q + b + 2>>; v >> };

        void h((int,int)->void a, int b) {
          a(1, b)
        };

        h(g, -1);
        h(f, -2);

        ''', '7 -1 6 -2')

    def test_return_func(self):
        self.base('''
        void f(int a) { a + 1>> };
        void g(int b) { b + 2>> };

        (int)->void h(int b) {
          if b == 1
            return f
          else
            return g
        };

        h(333)(1);
        h(1)(1);

        (int)->void a = h(333);
        a(4);
        ''', '3 2 6')

    def test_return_func_to_expr(self):
        self.base('''
        int c(int a) { return a + 1 };
        int f(int a) { return a + 1 };

        (int)->int g(int a, int b) {
          a + b >>;
          return f;
        };

        c(g(c(1), c(2))(c(1)) * 10) >>;
        ''', '5 31')

    def test_return_func_to_expr2(self):
        self.base('''
        int b () { return 1 };
        ()->int a(()->int f) { return f; };
        -a(b)() >>;
        ''', '-1')


class TestRead(unittest.TestCase):
    def base(self, src, expected_output, input_stream):
        stdout, stderr, rc = test(_compiler(src), input_stream)
        self.assertEqual(0, rc, "expect zero return code")
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_read(self):
        self.base('int a; >> a; a>>', '1', '1')

    def test_read_two(self):
        self.base('int a; int b; >> a; >>b; a + b>>', '3', '1 2')

    def test_read_negative(self):
        self.base('int a; >> a; a>>', '-1', '-1')

    def test_read_two_more_spaces(self):
        self.base('int a; int b; >> a; >>b; a + b>>', '3', '   1    2')

    def test_read_two_more_spaces_big_numbers(self):
        self.base('int a; int b; >> a; >>b; a + b>>', '53566866', '   32333233    21233633')

    def test_read_bool_true(self):
        self.base('bool a; >> a; a>>', 'true', ' t  ')

    def test_read_bool_false(self):
        self.base('bool a; >> a; a>>', 'false', ' f ')

    def test_read_two_bools(self):
        self.base('bool a; bool b; >> a; >>b; a>>; b>>', 'true false', ' t f ')


class BigTests(unittest.TestCase):
    # noinspection PyMethodMayBeStatic
    def test_big_file(self):
        build(os.path.join(os.path.dirname(__file__), '..', 'bigTest.it'))


if __name__ == '__main__':
    unittest.main()
