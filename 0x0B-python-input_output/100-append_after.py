#!/usr/bin/python3
"""
Module using method
"""


def append_after(filename="", search_string="", new_string=""):
    """method inserting text containing specified str line-by-line in file"""
    text = ""

    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
