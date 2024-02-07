#!/usr/bin/python3
"""
Module using method
"""
import json


def save_to_json_file(my_obj, filename):
    """method writing obj to text file utilising JSON format"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
