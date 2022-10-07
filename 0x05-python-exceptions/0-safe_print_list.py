#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    yoseph_variable = 0
    for yosephi in range(x):
        try:
            print(my_list[yosephi], end="")
            yoseph_variable += 1
        except IndexError:
            break
    print()
    return yoseph_variable
