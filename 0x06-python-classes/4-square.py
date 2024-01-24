#!/usr/bin/python3
"""Module for Square using class"""


class Square():
    """Square class"""

    def __init__(self, size=0):
        """
        Initialize Square
        Args:
            value (int): size of Square
        """
        self.__size = size

    @property
    def size(self):
        """
        Method for private size
        Returns:
            Private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Method for area of Square
        Returns:
            area of Square
        """
        return self.__size ** 2
