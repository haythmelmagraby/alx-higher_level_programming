#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter, printed = 0, 0
    while counter is not x:
        try:
            print("{:d}".format(my_list[counter]), end="")
        except (ValueError, TypeError):
            pass
        else:
            printed += 1
        finally:
            counter += 1
    print()
    return printed
