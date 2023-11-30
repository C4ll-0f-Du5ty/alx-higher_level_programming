#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    g = len(sys.argv)
    if g == 1:
        print("{} arguments.".format(0))
    else:
        print("{} arguments:".format(g - 1))
        for i in range(1, g):
            print("{}: {}".format(i, sys.argv[i]))
