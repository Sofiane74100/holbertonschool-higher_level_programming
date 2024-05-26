#!/usr/bin/python3
"""
    prints a square with the character #.
    one argument: size
    size is the size length of the sqaure
"""


def print_square(size):
    """
        prints a square with the character #.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
