#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    g = len(argv)
    sum = 0
    for i in range(1, g):
        sum += int(argv[i])
    print("{}".format(sum))
