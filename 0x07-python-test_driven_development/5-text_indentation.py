#!/usr/bin/python3
""" Divide a matrix"""


def text_indentation(text):

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for d in ".?:":
        text = (d + "\n\n").join([ln.strip(" ") for ln in text.split(d)])
        print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
