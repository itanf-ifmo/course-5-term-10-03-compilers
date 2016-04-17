import os
from subprocess import Popen, PIPE
import unittest

from compiler.settings import *
from compiler import compiler


def test(byte_code, stdin=None):
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    open(OUTPUT_FILE, 'wb').write(byte_code)
    p = Popen(["java", "A"], stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True, cwd=OUTPUT_DIR)

    if stdin:
        p.stdin.write(stdin)

    o, e = p.communicate()
    return o.decode("utf-8").strip(), e.decode("utf-8").strip()


class TestStringMethods(unittest.TestCase):
    def base(self, src, expected_output):
        stdout, stderr = test(compiler(src))
        self.assertEqual('', stderr, 'Expect empty stderr')
        self.assertEqual(expected_output, stdout)

    def test_empty(self):
        self.base('', '')

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

    def test_one(self):
        self.base('1 >>', '1')

    def test_1123333333(self):
        self.base('1123333333 >>', '1123333333')

    def test_minus_one(self):
        self.base('-1 >>', '-1')

    def test_not_minus_one(self):
        self.base('! -1 >>', 'true')

    def test_minus_true(self):
        self.assertRaisesRegex(Exception, 'Unexpected unary operator for boolean expression: -', compiler, '- true >>')


if __name__ == '__main__':
    unittest.main()
