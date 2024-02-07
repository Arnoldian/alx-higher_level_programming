#!/usr/bin/python3
"""
Module using class
"""


class Student:
    """class using methods"""

    def __init__(self, first_name, last_name, age):
        """method to instantiate"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method for directory description"""
        return self.__dict__.copy()
