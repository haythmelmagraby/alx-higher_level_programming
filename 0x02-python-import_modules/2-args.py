#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    print("{} arguments{}".format(
        len(args) - 1, ':' if len(args) - 1 > 0 else '.'))
    for i, a in enumerate(args):
        if i == 0:
            continue
        print("{}: {}".format(i, a))
