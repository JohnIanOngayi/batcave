#!/usr/bin/env python3


from collections.abc import Callable
from functools import wraps
from typing import Dict


class Apple:
    call_counts: Dict[str, int] = {}

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(*args, **kwargs):
            Apple.call_counts[method.__qualname__] = (
                Apple.call_counts.get(method.__qualname__, 0) + 1
            )
            method(*args, **kwargs)

        return wrapper

    def __init__(self, size: int = 2):
        self.size = size
        self.area = 4 * 3.142 * size * size

    @count_calls
    def call_apple(self):
        print("Booyah")


if __name__ == "__main__":
    a = Apple()
    qualname = a.call_apple.__qualname__
    a.call_apple()
    print(a.call_counts[qualname])
    a.call_apple()
    a.call_apple()
    print(a.call_counts[qualname])
