#!/usr/bin/env python3
import logging
import emp

logger = logging.getLogger()
file_handler = logging.FileHandler("calc.log")
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
file_handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def mul(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> float:
    return x / y


num_1, num_2 = 10, 5

add_res = add(num_1, num_2)
logger.debug(f"add {num_1} {num_2}: ans -> {add_res}")
sub_res = sub(num_1, num_2)
logger.debug(f"sub {num_1} {num_2}: ans -> {sub_res}")
mul_res = mul(num_1, num_2)
logger.debug(f"mul {num_1} {num_2}: ans -> {mul_res}")
div_res = div(num_1, num_2)
logger.debug(f"div {num_1} {num_2}: ans -> {div_res}")
