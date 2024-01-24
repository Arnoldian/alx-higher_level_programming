#!/usr/bin/python3
"""Module for Square using class"""


class Square():
    """Square class"""

    def __init__(self, size = 0):
        """
        Method to initialize Square
        Args:
            size (int): size of Square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method returning area of Square
        Returns:
            Square's area
        """
        return self.__size ** 2
