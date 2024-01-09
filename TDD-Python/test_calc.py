#usr/bin/python3

"""

This is na example module containing the tests for calc.py

"""

import unittest
from calc import add

class TestCalc(unittest.TestCase):

    def test_add_integers(self):
        result = add(10, 5)
        self.assertEqual(result, 15)

    def test_add_floats(self):
        result = add(16.9, 25.66)
        self.assertEqual(result, 41)

    def test_add_single(self):
        result = add(20.98)
        self.assertEqual(result, 118)

    def test_add_inf(self):
        self.assertRaises(OverflowError, add, float('inf'))
        self.assertRaises(OverflowError, add, float('inf'), float('inf'))
        self.assertRaises(OverflowError, add, float('inf'), 6)
        self.assertRaises(OverflowError, add, 6, float('inf'))
        self.assertRaises(OverflowError, add, float('inf'), 16.8)
        self.assertRaises(OverflowError, add, 16.8, float('inf'))

    def test_add_nan(self):
        self.assertRaises(ValueError, add, float('nan'))
        self.assertRaises(ValueError, add, float('nan'), float('nan'))
        self.assertRaises(ValueError, add, float('nan'), 6)
        self.assertRaises(ValueError, add, 6, float('nan'))
        self.assertRaises(ValueError, add, float('nan'), 16.8)
        self.assertRaises(ValueError, add, 16.8, float('nan'))
