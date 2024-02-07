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

    def to_json(self, attrs=None):
        """method for directory description with condition"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {h: getattr(self, h) for h in attrs if hasattr(self, h)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """method replacing all attributes of class instance"""
        for h, v in json.items():
            setattr(self, h, v)
