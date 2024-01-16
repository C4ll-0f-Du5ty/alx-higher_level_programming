#!/usr/bin/python3
"""A new Module called Base"""
import json


class Base:
    """declaring some attributes in the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Transforms our dictionary to a Json Repr."""
        return json.dumps(list_dictionaries)
