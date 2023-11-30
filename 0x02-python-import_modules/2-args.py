#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    g = len(argv) - 1

    print("{} arguments:".format(g) if g > 0 else "0 arguments.")
    for i in range(1, g):
        print("{}: {}".format(i, argv[i + 1]))
