#!/usr/bin/python3
'''Module is_same_class'''


def is_same_class(obj, a_class):
    ''' check if object is the same for a_class '''
    return type(obj) == a_class
