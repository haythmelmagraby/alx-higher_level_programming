#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    copylist = my_list.copy()
    copylist.sort()
    return copylist[-1]
