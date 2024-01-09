#!/usr/bin/python3
"""

This module is an introduction to unit testing in Python

"""

def add(x=0, y=98):
    """

    This function returns the sum of two numerics

    Args:
    x (int or float and optional):  first numeric, defaults to 0
    y (int or float and optional): second numeric, defaults to 0

    """
    if not isinstance(x, int) and not isinstance(x, float):
        raise TypeError("x must be an int or float")

    if not isinstance(y, int) and not isinstance(y, float):
        raise TypeError("y must be an int or float")

    return (int(x) + int(y))
