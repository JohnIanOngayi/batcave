#!/usr/bin/env python3

from typing import Callable, Dict, Optional, Sequence, Union, Any
from colorama import Fore
import redis  # type: ignore
from redis.typing import ResponseT  # type: ignore
import uuid
from functools import wraps


class Cache(object):

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def call_history(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args: Optional[Sequence], **kwargs: Optional[Dict]):
            qualname = method.__qualname__
            for arg in args:
                self._redis.rpush(f"{qualname}:inputs", arg)
            result = method(self, *args, **kwargs)
            self._redis.rpush(f"{qualname}:outputs", result)
            return result

        return wrapper

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        @wraps(method)
        def wrapper(self, *args: Optional[Sequence], **kwargs: Optional[Dict]):
            result = method(self, *args, **kwargs)
            qualname: str = method.__qualname__
            self._redis.incrby(qualname, 1)
            return result

        return wrapper

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float, Any]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[ResponseT, Any]:
        value = self._redis.get(key)
        if value and fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Union[ResponseT, str]:
        return self.get(key, lambda v: v.decode("utf-8"))

    def get_int(self, key: str) -> Union[ResponseT, int]:
        return self.get(key, lambda v: v.decode("utf-8"))

    def replay(self, method: Callable) -> None:
        qualname = method.__qualname__
        inputs = self._redis.lrange(f"{qualname}:inputs", 0, -1)
        outputs = self._redis.lrange(f"{qualname}:outputs", 0, -1)
        print(
            f"{method.__qualname__} was called {self._redis.get(method.__qualname__)} times"
        )
        for i, o in zip(inputs, outputs):
            print(
                "{}(*{}) -> {}".format(
                    method.__qualname__, i.decode("utf-8"), o.decode("utf-8")
                )
            )


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {b"foo": None, 123: int, "bar": lambda d: d.decode("utf-8")}

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
        print(Fore.GREEN + "Test Passed" + Fore.WHITE)
