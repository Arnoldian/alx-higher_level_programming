#!/usr/bin/python3
"""Module for Square through class"""


class Square:
    """Square - a class"""

    def __init__(self, size=0, position=(0, 0)):
        """
        initialize new Square
        Args:
            size (int): of new Square
            position (int, int): of new Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Method for present size of Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Method for present position of Square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method returns current area of Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """ Method for printing Square with # char """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Method for the print() of Square"""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):

            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]

            if i != self.__size - 1:
                print("")

        return ("")
