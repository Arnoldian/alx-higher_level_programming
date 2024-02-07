#!/usr/bin/python3
"""
Module using function
"""


def read_file(filename=""):
    """Method reads and prints contents of UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
