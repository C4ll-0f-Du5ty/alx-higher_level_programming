#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    g = len(argv)
    if g == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(g - 1) if g - 1 > 0 else "0 arguments.")
    for i in range(1, g):
        print("{}: {}".format(i, argv[i]))
