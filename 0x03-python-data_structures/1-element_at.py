#!/usr/bin/python3
def element_at(my_list, idx):
    yosephlist =  len(my_list) - 1
     if (idx < 0 or idx > yosephlist):
         return (None)
     else:
         return (my_list[idx])
