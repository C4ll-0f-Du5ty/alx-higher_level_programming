#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    k = len(my_list)
    new_list = []
    for i, x in enumerate(my_list):
        if x % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
