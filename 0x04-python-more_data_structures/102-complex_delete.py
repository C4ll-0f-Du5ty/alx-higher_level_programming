#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ls = [key for key, j in a_dictionary.items() if j == value]
    for key in ls:
        del (a_dictionary[key])
    return a_dictionary
