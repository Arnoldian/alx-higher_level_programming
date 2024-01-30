#!/usr/bin/python3
"""
Module with class Rectangle
"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method for comparing Rectangle instances"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

     @classmethod
    def square(cls, size=0):
        """method for Rectangle instant height==width"""
        return cls(size, size)

    def __init__(self, width=0, height=0):
        """method for init/instantiation"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """method width"""
        return (self.__width)

    @property
    def height(self):
        """method height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method perimiter"""
        if self.__width is 0 or self.__height is 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """method for str repr of Rectangle"""
        if self.__width is 0 or self.__height is 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
            for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """method for str repr of Rectangle (formal)"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """method for deleted instance message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
