#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list or not idx:
        return None
    my_list.remove(my_list[idx])
    return my_list
