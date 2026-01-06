#!/usr/bin/env python3
"""Funcion to get elements and their lengths"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing elements and their lengths

    Args:
    lst (Iterable[Sequence]): an iterable of sequence elements

    Returns:
    List[Tuples[Sequence, int]]: list of tuples (element, length)
    """
    return [(i, len(i)) for i in lst]
