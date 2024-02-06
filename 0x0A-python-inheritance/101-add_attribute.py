#!/usr/bin/python3
"""
Module using method
"""


def add_attribute(obj, attribute, value):
    """method adding new attribute to obj when possible"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value
