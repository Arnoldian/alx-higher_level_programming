#!/usr/bin/python3
"""Module for Square using class"""


class Square():
    """square class with self size"""

    def __init__(self, size=0):
        """
        Method initializing Square
        Args:
            size (int): of Square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
