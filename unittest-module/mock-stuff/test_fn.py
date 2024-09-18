#!/usr/bin/env python3

import unittest
from unittest.mock import Mock, patch

"""Mocking a function"""


def my_function():
    return "real value"


class test_fn_mock(unittest.TestCase):

    @patch("__main__.my_function")
    def test_mocked_fn(self, mocked_fn: Mock):
        mocked_fn.return_value = "Booyahh!!!"
        self.assertEqual(my_function(), "Booyahh!!!")


if __name__ == "__main__":
    unittest.main()
