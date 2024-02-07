#!/usr/bin/python3
"""
Module using method
"""
import json


def load_from_json_file(filename):
    """method creates Py obj from specified JSON file"""
    with open(filename) as f:
        return json.load(f)
