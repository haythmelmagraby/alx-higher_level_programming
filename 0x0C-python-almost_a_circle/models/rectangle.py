#!/usr/bin/python3
'''Rectangel Module'''
from models.base import Base


class Rectangle(Base):
    '''Content of Rectangle Class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''the Constructor'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @width.setter
    def width(self, value):
        '''width setter'''
        self.setter_validation('width', value, True)
        self.__width = value

    @height.setter
    def height(self, value):
        '''height setter'''
        self.setter_validation('height', value, True)
        self.__height = value

    @x.setter
    def x(self, value):
        '''x setter'''
        self.setter_validation('x', value, False)
        self.__x = value

    @y.setter
    def y(self, value):
        '''y setter'''
        self.setter_validation('y', value, False)
        self.__y = value

    def setter_validation(self, name, v, iswh):
        '''setter validation'''
        if type(v) != int:
            raise TypeError("{} must be an integer".format(name))

        if iswh and v <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not iswh and v < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        '''calc rectangle area'''
        return self.width * self.height

    def display(self):
        '''display rectangle'''
        rect = '\n' * self.y + (' ' * self.x + '#' * self.width + '\n') \
               * self.height
        print(rect, end='')

    def __str__(self):
        '''rectangle informations'''
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x,
                                                self.y, self.width,
                                                self.height)

    def __param_update(self, id=None, width=None, height=None, x=None, y=None):
        '''private update parameters'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''attributes update'''
        if args:
            self.__param_update(*args)

        if kwargs:
            self.__param_update(**kwargs)

    def to_dictionary(self):
        '''Rectangle instance to dictionary'''
        return {"x": self.__x, "width": self.__width, "id": self.id,
                "height": self.__height, "y": self.__y}

    def to_dictionary_rearrange(self):
        '''Rectangle instance to dictionary'''
        return {"y": self.__y, "x": self.__x, "width": self.__width,
                "id": self.id, "height": self.__height}
