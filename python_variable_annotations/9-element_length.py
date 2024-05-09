#!/usr/bin/env python3
"""element length function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list with a string and number"""
    return [(i, len(i)) for i in lst]
