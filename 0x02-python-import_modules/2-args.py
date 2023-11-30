#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    g = len(argv)
    if g == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(g - 1))
        for i in range(1, g):
            print("{}: {}".format(i, argv[i]))
