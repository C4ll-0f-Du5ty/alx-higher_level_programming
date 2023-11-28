#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if 123 > ord(str[i]) > 96:
            k = ord(str[i]) - 32
            print("{:c}".format(k), end="")
        elif 91 > ord(str[i]) > 64:
            print("{:c}".format(ord(str[i])), end="")
        else:
            print(str[i], end="")
    else:
        print("")
