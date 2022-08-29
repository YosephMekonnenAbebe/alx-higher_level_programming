#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    yosephlist = en(my_list) - 1
    if (idx < 0 or idx > yosephlist):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
