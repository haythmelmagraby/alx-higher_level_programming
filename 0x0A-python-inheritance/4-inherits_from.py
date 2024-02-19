#!/usr/bin/python3
'''Module Lookup module '''


def inherits_from(obj, a_class):
    ''' check class that inherited (directly or indirectly) '''
    return isinstance(obj, a_class) and (type(obj) != a_class)
