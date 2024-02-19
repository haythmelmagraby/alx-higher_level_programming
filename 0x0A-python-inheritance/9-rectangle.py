#!/usr/bin/python3
'''Module for Rectangle '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Rectangle is subclass to BaseGeometry'''
    def __init__(self, width, height):
        '''Rectangle constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        '''area implementation'''
        return self.__height * self.__width

    def __str(self):
        '''string impelementation '''
        return ["[Rectangle] " + str(self.__width) + "/" + str(self.__height)]
