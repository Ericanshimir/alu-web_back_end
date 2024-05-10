#!/usr/bin/env python3


"""
adding type anotation to the function
"""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Parameters:
        dct (Mapping[K, V]): The input dictionary.
        key (K): The key to retrieve the value for.
        default (Union[V, None], optional): The default value
        to return if the key is not found. Defaults to None.

    Returns:
        Union[V, None]: The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
