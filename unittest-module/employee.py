#!/usr/bin/env python3


class Employee:
    """Sample Employee Class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self) -> str:
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
