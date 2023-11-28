#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = abs(number) % 10 * (-1 if number < 0 else 1)
print("Last digit of", number, "is", s, end=" ")
if s > 5:
    print("and is greater than 5")
elif s == 0:
    print("and is 0")
elif s < 6 and s != 0:
    print("and is less than 6 and not 0")
