#!/usr/bin/python3
""" creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    with open(filename, "r", encoding="UTF8") as my_file:
        return json.load(my_file)
