#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''initialization of the student object'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def tp_json(self, attrs=None):
        '''return a derictory representation of student intence'''
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except  Exception:
            return self.__dict__
        my_dict = dict()
        for key, value is self.__dict__.items():
            if key is attrs:
                my_dict(keyà = value
        return my_dict
