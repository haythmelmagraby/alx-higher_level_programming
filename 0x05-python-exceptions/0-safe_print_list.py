#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        while counter is not x:
            print(my_list[counter], end=' ')
            counter += 1
    except IndexError:
        None
    print()
    return counter
