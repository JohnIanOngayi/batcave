#!/usr/bin/env python3
from typing import Callable


def add_sprinkles(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("No sprinkles yet")
        func(*args, **kwargs)
        print("Yaay sprinkles🎊")

    return wrapper


def add_fudge(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("1 Fudge")
        func(*args, **kwargs)
        print("2 Fudge")

    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flavour: str):
    print(f"Here's your {flavour} icecream")


if __name__ == "__main__":
    get_ice_cream("vanilla")
