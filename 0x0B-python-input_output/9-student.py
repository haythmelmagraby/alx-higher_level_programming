#!/usr/bin/python3
""" class Student Module """


class Student:
    """ represent student """
    def __init__(self, first_name, last_name, age):
        """ student constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return json dictionary """
        return self.__dict__
