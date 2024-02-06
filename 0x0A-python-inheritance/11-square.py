#!/usr/bin/python3
"""
Module for subclass Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class for Square"""

    def __init__(self, size):
        """method for initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """method for str"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """method for area"""
        return self.__size ** 2
