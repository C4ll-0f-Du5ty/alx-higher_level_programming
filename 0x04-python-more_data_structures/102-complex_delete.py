#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l = [key for key , j in a_dictionary.items() if j == value]
    for key in l:
        del (a_dictionary[key])
    return a_dictionary            
