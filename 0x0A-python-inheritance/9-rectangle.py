#!/usr/bin/python3
"""
Module using subclass Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inheriting from BaseGeometry class"""

    def __init__(self, width, height):
    """method for initialization"""
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
    """method for area"""
        return self.__width * self.__height

    def __str__(self):
    """method for string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
