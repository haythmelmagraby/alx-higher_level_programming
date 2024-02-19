#!/usr/bin/python3
'''Module for BaseGeometry '''


class BaseGeometry:
    ''' BaseGeometry class '''
    def area(self):
        '''raises an Exception with the message'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''that validates value'''
        if(type(value) != int):
            raise TypeError('{} must be an integer'.format(name))

        if(value <= 0):
            raise ValueError('{} must be greater than 0'.format(name))
