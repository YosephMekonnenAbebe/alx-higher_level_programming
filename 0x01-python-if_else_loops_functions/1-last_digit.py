#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (abs(number) % 10) > 5 and number > 0:
    print(f"Last digit of {number:d} is {abs(number) % 10:d} and is greater than 5")
elif (abs(number) % 10) == 0:
    print(f"Last digit of {number:d} is {abs(number) % 10:d} and is 0")
elif (abs(number) % 10) < 6 and (abs(number) % 10) != 0 or number < 0:
    if number > 0:
        print(f"Last digit of {number:d} is {abs(number) % 10:d} and is less than 6 and not 0")
    elif number < 0:
        print(f"Last digit of {number:d} is {-(abs(number) % 10):d} and is less than 6 and not 0")
