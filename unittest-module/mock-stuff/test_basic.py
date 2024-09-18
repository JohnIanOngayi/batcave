#!/usr/bin/env python3

import unittest
from unittest.mock import Mock

"""Basic mock object"""


class simple_mock(unittest.TestCase):
    def test_verify_simple_mock(self):
        my_mock = Mock()

        my_mock.return_value = 56

        result = my_mock()

        assert result == 56


if __name__ == "__main__":
    unittest.main(verbosity=2)
