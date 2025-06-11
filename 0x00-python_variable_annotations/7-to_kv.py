#!/usr/bin/env python3
from typing import Tuple, Union

"""Contains a func that returns a tuple of it arguments"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    a = k, v
    return a
