#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    myD = a_dictionary.copy()
    for k in myD:
        myD[k] *= 2
    return myD
