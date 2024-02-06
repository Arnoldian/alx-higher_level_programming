#!/usr/bin/python3
"""
Module using class
"""


class BaseGeometry:
    """class using methods"""

    def area(self):
        """method raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method validates integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
