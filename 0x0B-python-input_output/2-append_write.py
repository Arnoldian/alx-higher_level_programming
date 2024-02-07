#!/usr/bin/python3
"""
Module using method
"""


def append_write(filename="", text=""):
    """method appends to end of UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
