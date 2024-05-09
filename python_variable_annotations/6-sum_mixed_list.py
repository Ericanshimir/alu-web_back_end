#!/usr/bin/env python3
"""mixed list function"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of mixed numbers"""
    return sum(mxd_lst)
