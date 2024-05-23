#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Class Square with a size attribute."""
    def __init__(self, size=0):
        """
            Initialize a new instance of the Square class.
            size (int): The size of the square initialize at 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    """public class Square."""
    def area(self):
        return self.__size ** 2
