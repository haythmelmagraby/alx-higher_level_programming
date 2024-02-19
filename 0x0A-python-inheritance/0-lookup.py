#!/usr/bin/python3
'''Module Lookup module '''


def lookup(obj):
    '''lookup of available attributes and methods of an object.
    Args:
        obj: object to get list of.

    Returns:
        list: list of attributes and methods.
    '''
    return dir(obj)
