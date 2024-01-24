#!/usr/bin/python3
"""Module for Square using class"""


class Square():
    """Square - a class"""

    def __init__(self, size=0):
        """
        init Square
        Args:
            value (int): size of Square
        """
        self.size = size

    @property
    def size(self):
         """
         size (int): private size
        Returns:
            Private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        value (int) into size
        Args:
            value (int): size of Square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """
        Method for area of Square
        Returns:
            area of Square
        """
        return self.__size**2

    def my_print(self):
        """Method for printing in stdout Square with # char"""
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
