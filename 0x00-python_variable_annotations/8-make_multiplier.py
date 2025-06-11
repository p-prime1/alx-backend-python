#!/usr/bin/env python3

from typing import Callable

"""Module contains a function that multiplies a value"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Funtion accepts a func and multiplied the value by multiplier"""

    def new_func(value: float) -> float:
        return multiplier * multiplier

    return new_func
