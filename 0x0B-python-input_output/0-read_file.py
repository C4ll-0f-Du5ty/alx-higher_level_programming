#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, encoding='UTF_8') as file:
        print(file.read(), end="")

