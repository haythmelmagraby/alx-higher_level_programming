#!/usr/bin/python3
'''Module for MyInt '''


class MyInt(int):
    '''MyInt  rebel Class'''
    def __new__(cls, *args, **kwargs):
        '''instance from parent class'''
        return super(MyInt, cls).__new__(cls, *args, **kwargs)
        

    def __eq__(self, another):
        '''reverse equale'''
        return int(self) != another

    def __ne__(self, another):
        '''reverse not equale'''
        return int(self) == another
