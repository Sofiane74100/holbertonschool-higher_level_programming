#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Class Square with a size attribute."""
    def __init__(self, size=0):
        self.size = size
    """Getter for retrieving the value of the private attribute 'size'"""
    @property
    def size(self):
        return self.__size
    """Setter method for setting the value of the private attribute 'size'"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """public class Square."""
    def area(self):
        return self.__size ** 2
