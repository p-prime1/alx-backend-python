#!/usr/bin/env python3
from typing import List, Union

"""Module contains a func that returns sum of list"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Accepts a list of int and float and returns a float"""
    a: float = 0
    for i in mxd_lst:
        a += i
    return a
