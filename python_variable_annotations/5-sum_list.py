#!/usr/bin/env python3
"""Function to make the sum of a list of floats"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Claculates the sum of a list of floats

    Args:
    input_list: A list of float numbers

    Returns:
    The sum of thee numbers in the list as a float
    """
    
    return sum(input_list)
