#!/usr/bin/env python3

from typing import Callable, Optional, Sequence, Mapping
from functools import wraps
import requests  # type: ignore
import redis  # type: ignore


r = redis.Redis()


def call_counts(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(*args: Optional[Sequence], **kwargs: Optional[Mapping]):
        result = method(*args, **kwargs)
        r.incrby(f"count:{args}", 1)
        r.setex(f"result:{args}", 10, result)
        return result

    return wrapper


def get_page(url: str) -> str:
    result = requests.get(url)
    return result.text
