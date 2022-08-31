#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for yosephx, yosephy in list(a_dictionary.items()):
        if yosephy is value:
            a_dictionary.pop(yosephx)
    return a_dictionary
