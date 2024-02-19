#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    '''Raise a TypeError exception if can't add attr'''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
