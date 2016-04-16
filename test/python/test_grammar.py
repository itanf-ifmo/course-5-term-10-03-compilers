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

    def test_print_true(self):
        self.base('true >>', '1')

    def test_print_false(self):
        self.base('false >>', '0')

    def test_print_boolean_un_op_not1(self):
        self.base('!true >>', '0')

    def test_print_boolean_un_op_not2(self):
        self.base('not true >>', '0')

    def test_print_boolean_un_op_not3(self):
        self.base('! false >>', '1')

    def test_print_boolean_un_op_not4(self):
        self.base('not false >>', '1')

    # def test_print_boolean_op_and(self):
    #     self.base('true && true >>', '')


if __name__ == '__main__':
    unittest.main()
