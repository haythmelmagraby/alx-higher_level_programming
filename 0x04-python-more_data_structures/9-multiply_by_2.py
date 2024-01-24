#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {key: a_dictionary[key] * 2 for key in iter(a_dictionary)}
    return new_d
