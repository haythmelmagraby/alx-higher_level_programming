#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        arg = fct(*args)
        return arg
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return None
