#!/usr/bin/python3
'''Module check the same '''


def is_same_class(obj, a_class):
    ''' check if object is the same for a_class '''
    if (type(obj) == a_class):
        return True
    else:
        return False
