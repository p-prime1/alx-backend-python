#!/usr/bin/env python3
"""Module contains a func that adds list of floats"""


def sum_list(input_list: list[float]) -> float:
    """Function accepts list of float and returns the sum of them (float)"""
    a: float = 0
    for i in input_list:
        a += i
    return a
