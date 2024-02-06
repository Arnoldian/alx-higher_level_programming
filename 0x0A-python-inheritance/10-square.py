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
