import unittest
from mymath.factorial import factorial


class TestFactorialFunctions(unittest.TestCase):

    def test_3(self):
        self.assertEqual(factorial(3), 6)
