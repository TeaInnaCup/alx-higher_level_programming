#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
exe = 1 if number < 0 else 0
last_digit = int((number_str[-1:]))
if exe:
    number_str = number_str[:-1]
    number = int(number_str)
    last_digit *= -1
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
