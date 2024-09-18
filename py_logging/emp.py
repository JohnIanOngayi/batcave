#!/usr/bin/env python3

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("employee.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# logging.basicConfig(
#     filename="emp.log", level=logging.INFO, format=
# )


class Employee:
    def __init__(self, first: str, last: str) -> None:
        self.first = first
        self.last = last

        logger.info(f"Created Employee: {self.fullname} - {self.email}")

    @property
    def email(self) -> str:
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"


emp_1 = Employee("Correy", "Schafer")
emp_2 = Employee("John", "Doe")
emp_3 = Employee("Jane", "Doe")
