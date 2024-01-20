#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    new_string = ""
    for i in range(len(my_string)):
        if my_string[i].lower() != 'c':
            new_string += my_string[i]
    return new_string
