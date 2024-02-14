#!/usr/bin/python3
"""Print square"""


def print_square(size):

    if not isinstance(size, int) or len(matrix) == 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be an integer")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
