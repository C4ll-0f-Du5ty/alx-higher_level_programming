#!/usr/bin/python3
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end="\n" if i == ord('Z') else "")
