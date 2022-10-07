#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    yoseph_variable = 0
    for yosephi in range(x):
        try:
            print("{:d}".format(my_list[yosephi]), end="")
            yoseph_variable += 1
        except (ValueError, TypeError):
            continue
    print()
    return yoseph_variable
