#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest = 0
    bigkey = None
    for k in a_dictionary:
        if a_dictionary[k] > biggest:
            biggest = a_dictionary[k]
            bigkey = k
    return bigkey
