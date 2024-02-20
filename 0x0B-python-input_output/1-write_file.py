#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file"""
    with open(filename, "w", encoding="UTF8") as my_file:
        return my_file.write(text)
