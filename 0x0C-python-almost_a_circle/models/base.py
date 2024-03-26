#!/usr/bin/python3
'''Base Module'''
from json import dumps
from json import loads
from os import path


class Base:
    '''Content of Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Dictionary to JSON'''
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''JSON string to file'''
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]

        with open("{}.json".format(cls.__name__),
                  "w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        '''JSON string to dictionary'''
        if not json_string or json_string is None:
            return []
        else:
            return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Dictionary to Instance'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Square:
            ins = Square(1)
        elif cls is Rectangle:
            ins = Rectangle(1, 1)
        else:
            ins = None

        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        '''File to instances'''
        file = "{}.json".format(cls.__name__)
        if path.isfile(file):
            with open(file, "r", encoding="utf-8") as my_file:
                return [cls.create(**i) for i in
                        cls.from_json_string(my_file.read())]
        else:
            return []
