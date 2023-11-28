#!/usr/bin/env python3
def islower(c):
    if 91 > ord(c) > 64:
        return False
    elif 123 > ord(c) > 96:
        return True
