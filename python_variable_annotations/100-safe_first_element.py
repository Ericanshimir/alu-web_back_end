#!/usr/bin/env python3


"""
import Sequence, Union and Any from typing
correct duck-typed annotations
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function safe_first_element
    parameters
        lst: list
    """
    if lst:
        return lst[0]
    else:
        return None
