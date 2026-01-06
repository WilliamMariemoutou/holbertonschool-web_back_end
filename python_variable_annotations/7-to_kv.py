#!/usr/bin/env python3
"""Function to convert a
string and an int or float value into a tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and an int or float value into a tuple

    Args:
    k: The string key
    v: The value (int or float) to be squared

    Returns:
    A tuple containing the key and the squared value as a float
    """
    squared_v: float = float(v ** 2)
    return (k, squared_v)
