#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    yoseph_list = []
    for yosephnum in my_list:
        if (yosephnum % 2) == 0:
            yoseph_list.append(True)
        else:
            yoseph_list.append(False)
    return(yoseph_list)
