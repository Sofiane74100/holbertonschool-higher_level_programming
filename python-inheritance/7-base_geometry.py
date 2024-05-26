#!/usr/bin/python3
"""
    create an empty class
"""


class BaseGeometry:
    """
        Public instance method
    """

    def area(self):
        """method for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method for validate if a num is integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
