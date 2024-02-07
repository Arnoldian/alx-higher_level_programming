#!/usr/bin/python3
"""
Module using method
"""
import json


def from_json_string(my_str):
    """method for Py obj representation of JSON str"""
    return json.loads(my_str)
