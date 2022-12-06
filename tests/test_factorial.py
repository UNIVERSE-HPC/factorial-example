import unittest
from mymath.factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_3(self):
        self.assertEqual(factorial(3), 6)

    def test_5(self):
        self.assertEqual(factorial(5), 120)
