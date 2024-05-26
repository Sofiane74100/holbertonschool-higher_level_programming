#!/usr/bin/python3
"""area and perimeter rectangle"""


class Rectangle:
    """define a class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        perimeter = (self.__width + self.__height) * 2
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return perimeter

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rec = ""
            for _ in range(self.__height):
                rec += str(self.print_symbol) * self.__width + "\n"
            return rec.rstrip("\n")

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        Area_rect_1 = rect_1.__width * rect_1.__height
        Area_rect_2 = rect_2.__width * rect_2.__height

        if Area_rect_1 >= Area_rect_2:
            return rect_1
        else:
            return rect_2
