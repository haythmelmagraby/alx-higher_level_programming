#!/usr/bin/python3
""" Square Module """


class Square:
    """ Define a square """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or not all(isinstance(n, int) for n in value) 
            or len(value) != 2 or not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
            return

        for i in range(0, self.position[1]):
            print()

        for i in range(0, self.__size):
            for n in range(0, self.__position[0]):
                print("_", end="")
            for s in range(0, self.__size):
                print("#", end="")
            print("$")
