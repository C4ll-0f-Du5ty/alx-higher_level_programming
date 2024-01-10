#!/usr/bin/python3
"""Student module to Json"""


class Student:
    """retrieves a dictionary representation of a Student instance"""
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
