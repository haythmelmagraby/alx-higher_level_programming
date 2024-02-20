#!/usr/bin/python3
''' class Student Module '''


class Student:
    ''' class Student '''
    def __init__(self, first_name, last_name, age):
        ''' student constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' return json dictionary '''
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dic = dict()

        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value

        return dic

    def reload_from_json(self, json):
        ''' that replaces all attributes of the Student instance '''
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
