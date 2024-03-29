#!/usr/bin/python3

""" Module for a circle using a class"""
import math


class MagicClass:
    """MagicClass - a circle class"""

    def __init__(self, radius=0):
        """Method for making use of radius

        Arg:
            radius (float or int): of new MagicClass"""
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """method for calculating area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Method for calculating circumference"""
        return 2 * math.pi * self.__radius
