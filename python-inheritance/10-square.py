#!/usr/bin/python3
"""
    create an empty class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        class square that inherits from rectangle.
    """

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        self.integer_validator("size", self.__size)

    def __str__(self):
        """
            Return the square description.
        """
        return f"[Rectangle] {self.__size}/{self.__size}"

    def area(self):
        """
            Method to calculate the area of the square.
        """
        return self.__size ** 2
