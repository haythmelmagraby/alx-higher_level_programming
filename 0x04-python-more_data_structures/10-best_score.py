#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    key_val = ""
    for key in iter(a_dictionary):
        if a_dictionary[key] > max:
            max = a_dictionary[key]
            key_val = key
    return key_val
