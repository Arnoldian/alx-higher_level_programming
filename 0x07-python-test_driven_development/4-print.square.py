#!/usr/bin/python3
"""
Module for printing square with method
"""


def print_square(size):
    """method for printing square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
