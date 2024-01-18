#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) - 1 == 0:
        print("0 arguments.")
    elif len(args) - 1 == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(args) - 1))
    for i, a in enumerate(args):
        if i == 0:
            continue
        print("{}: {}".format(i, a))
