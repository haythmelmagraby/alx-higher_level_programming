#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, "w", encoding="UTF8") as my_file:
        json.dump(my_obj, my_file)
