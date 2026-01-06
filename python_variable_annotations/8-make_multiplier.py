#!/usr/bin/env python3
"""Creates a function that multiplies a float by a given multiplier"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable [[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier
    
    Args:
    multiplier: The value to multiply by
    
    Returns:
    A function that takes a float and returns float
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    
    return multiplier_function
