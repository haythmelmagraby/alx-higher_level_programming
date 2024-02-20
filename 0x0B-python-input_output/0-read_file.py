#!/usr/bin/python3
"""reads a text file"""


def read_file(filename=""):
    with open(filename, encoding="UTF8") as my_file:
        print(my_file.read(), end="")
