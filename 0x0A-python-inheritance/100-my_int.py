#!/usr/bin/python3
"""
Module using class inheriting from int
"""


class MyInt(int):
    """class using methods"""

    def __eq__(self, other):
    """method for eq"""
        return int(str(self)) != other

    def __ne__(self, other):
    """method for ne"""
        return int(str(self)) == other
