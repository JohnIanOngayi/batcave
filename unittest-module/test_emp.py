#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.emp_1 = Employee("John", "Doe", 650_000)
        self.emp_2 = Employee("Jane", "Doe", 460_000)

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

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

    def test_monthly_schedule(self):
        with patch("requests.get") as mocked_get:

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Doe/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Doe/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
