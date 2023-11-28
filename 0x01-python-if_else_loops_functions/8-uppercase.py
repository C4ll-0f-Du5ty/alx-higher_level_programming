#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if 123 > ord(str[i]) > 96:
            k = ord(str[i]) - 32
            print("{:c}".format(k), end="" if i != len(str) - 1 else "\n")
        else:
            print(str[i], end="" if i != len(str) - 1 else "\n")
