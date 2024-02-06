#!/usr/bin/python3
"""
Module using class MyList
"""


class MyList(list):
    """class inheriting from list"""

    def print_sorted(self):
        """method for ascending list"""
        print(sorted(self))
