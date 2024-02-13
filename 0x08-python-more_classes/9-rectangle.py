#!/usr/bin/python3
""" Write an empty class Rectangle that defines a rectangle """


class Rectangle:
    """ Rectangle Class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
    """ Rectangle Class"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
    """ Rectangle Class"""
        return self.__height

    @height.setter
    def height(self, value):
    """ Rectangle Class"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
    """ Rectangle Class"""
        return self.__width

    @width.setter
    def width(self, value):
    """ Rectangle Class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
    """ Rectangle Class"""
        return self.__height * self.__width

    def perimeter(self):
    """ Rectangle Class"""
        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
    """ Rectangle Class"""
        result = ""
        if (self.__height != 0 and self.__width != 0):
            result += ((str(self.print_symbol) * self.__width +
                        "\n") * self.__height)[:-1]
        return result

    def __repr__(self):
    """ Rectangle Class"""
        result = "Rectangle({:d}, {:d})".format(self.__width, self.__height)
        return result

    def __del__(self):
    """ Rectangle Class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
    """ Rectangle Class"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        ''' Class method
        Args:
            size: size of the square.
        '''
        return cls(size, size)
