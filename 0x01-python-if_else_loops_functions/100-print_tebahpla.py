#!/usr/bin/python3
letter = 122
while letter >= 97:
    flag = 0
    print("{:s}".format(chr(letter - (32 if letter % 2 != 0 else 0))), end="")
    letter = letter - 1
print()
