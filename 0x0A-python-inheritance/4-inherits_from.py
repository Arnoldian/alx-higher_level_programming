#!/usr/bin/python3
"""
Module using method
"""


def inherits_from(obj, a_class):
    """method checking is subclass and inherits"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
