#!/usr/bin/python3
def islower(c):
    if ord('Z') >= ord(c) >= ord('A'):
        return False
    elif 123 > ord(c) > 96:
        return True


def uppercase(str):
    for i in str:
        print("{:c}".format(ord(i) if not islower(i) else ord(i) - 32), end="")
    print("")
