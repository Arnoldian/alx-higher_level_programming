#!/usr/bin/python3
"""
Module using method
"""


def write_file(filename="", text=""):
    """method writing to UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
