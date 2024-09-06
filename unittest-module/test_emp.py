#!/usr/bin/env python3

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    emp_1 = Employee("John", "Doe", 650_000)
    emp_2 = Employee("Jane", "Doe", 460_000)

    def test_email(self):
        self.assertEqual(self.emp_1.email, "John.Doe@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Doe@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "John Doe")
        self.assertEqual(self.emp_2.fullname, "Jane Doe")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(1.05 * 650_000, self.emp_1.pay)
        self.assertEqual(1.05 * 460_000, self.emp_2.pay)


if __name__ == "__main__":
    unittest.main()
