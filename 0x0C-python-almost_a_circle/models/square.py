#!/usr/bin/python3
'''Square Moadule'''
from models.rectangel import Rectangel


class Square(Rectangel):
    '''Content of Square Sub Class'''
    def __init__(self, size, size, x=0, y=0, id=None):
        '''the Constructor'''
        super().__init__(size, size, x, y, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''rectangle informations'''
        return "[{}] () {}/{} - {}".format(type(self)__name__,
                                              self.id, self.x,
                                              self.y, self.width)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size sitter'''
        self.width = value
        self.height = value

    def __param_update(self, id=None, size=None, x=None, y=None):
        '''private update parameters'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''attributes update'''
        if args:
            self.__param_update(args)

        if kwargs:
            self.__param_update(kwargs)
