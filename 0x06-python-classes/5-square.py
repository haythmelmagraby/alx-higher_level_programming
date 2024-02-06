#!/usr/bin/python3
""" Square Module """


class Square:
    """ Define a square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=0):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            for n in range(self.size):
                print("#", end="\n" if n is self.size - 1 and i != n else "")
        print()
