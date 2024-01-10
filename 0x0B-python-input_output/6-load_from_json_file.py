#!/usr/bin/python3
"""creating an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """creating an Object from a “JSON file”"""
    with open(filename) as f:
        return json.load(f)
