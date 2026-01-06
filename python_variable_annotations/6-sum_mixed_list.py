#!/usr/bin/env python3
"""Function to calculate the sum of a mixed list of integers and floats"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a mixed list of integers and floats

    Args:
    mxd_lst: A list containing both integers and floats

    Returns:
    The sum of all numbers in the list as a float
    """
    return float(sum(mxd_lst))
