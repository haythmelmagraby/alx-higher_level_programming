#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function that appends a string"""
    with open(filename, "a", encoding="UTF8") as my_file:
        return my_file.write(text)
