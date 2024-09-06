#!/usr/bin/env python3

from calc import add, subtract, multiply, divide
import unittest
from unittest.mock import Mock


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5.9, add(2.1, 3.8))
        self.assertEqual(59, add(21, 38))
        self.assertEqual(-1 + -1, add(-1, -1))

    def test_sub(self):
        self.assertEqual(4.5 - 6.5, subtract(4.5, 6.5))
        self.assertEqual(40 - 20, subtract(40, 20))
        self.assertEqual(-40 - -20, subtract(-40, -20))

    def test_mul(self):
        self.assertEqual(10 * 0, multiply(10, 0))
        self.assertEqual(0.5 * 5.5, multiply(0.5, 5.5))
        self.assertEqual(2 * 2, multiply(2, 2))
        self.assertEqual(-2.7 * -2.7, multiply(-2.7, -2.7))

    def test_div(self):
        with self.assertRaises(ValueError):
            divide(9, 0)


if __name__ == "__main__":
    unittest.main()
