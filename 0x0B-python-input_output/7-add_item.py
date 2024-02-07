#!/usr/bin/python3
"""
Module adding all args to Py list and saving to file
"""
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


if __name__ == "__main__":
    #save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    #load_from_json_file = \
     #   __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
