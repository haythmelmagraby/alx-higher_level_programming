#!/usr/bin/python3
'''Module for Square '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Square is subclass to BaseGeometry'''

    def __init__(self, size):
        '''Square constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''calc Square area'''
        return self.__size ** 2
