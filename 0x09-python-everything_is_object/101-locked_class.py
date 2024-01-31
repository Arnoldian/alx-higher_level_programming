#!/usr/bin/python3
"""
Module LockedClass
"""


class LockedClass:
    """allows only instantiation of attr first_name"""

    __slots__= ['first_name']
