#!/usr/bin/python3
"""
    verify if a is an integer or a float
    converts float to int
    result: sum of 2 integer
"""


def add_integer(a, b=98):
    """
        verify if a is an integer or a float
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
