#!/usr/bin/python3
'''Base Module'''
import json


class Base:
    '''Content of Base Class'''
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objets

    def to_json_string(list_dictionaries):
        '''Dictionary to JSON'''
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return dumps(list_dictionaries)
