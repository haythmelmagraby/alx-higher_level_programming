#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    result = True
    try:
        print("{:d}".format(value))
    except Exception as ex:
        print("Exception:", ex, file=sys.stderr)
        result = False
    return result
