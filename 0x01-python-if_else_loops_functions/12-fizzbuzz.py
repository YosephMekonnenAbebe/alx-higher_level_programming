#!/usr/bin/python3
def fizzbuzz():
    colon = " "
    for yoseph in range(1, 101):
        if yoseph % 3 == 0 and yoseph % 5 != 0:
            print("Fizz", end=colon)
        elif yoseph % 5 == 0 and yoseph % 3 != 0:
            print("Buzz", end=colon)
        elif (yoseph % 3 == 0) and (yoseph % 5 == 0):
            print("FizzBuzz", end=colon)
        else:
            if yoseph == 99:
                colon = ""
            print(yoseph, end=colon)
