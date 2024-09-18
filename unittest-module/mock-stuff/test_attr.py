#!/usr/bin/env python3

import unittest
from unittest.mock import patch

"""Mocking an attribute"""


class MyClass:
    my_attr = "real value"


class test_attr_mock(unittest.TestCase):

    # @patch("__main__.MyClass.my_attr", "Booyahh!!!")
    def test_attr_mock(self):
        with patch("__main__.MyClass.my_attr", "Booyahh!!!"):
            test_obj = MyClass()
            self.assertEqual(test_obj.my_attr, "Booyahh!!!")


if __name__ == "__main__":
    unittest.main()
