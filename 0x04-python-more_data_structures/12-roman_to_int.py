#!/usr/bin/python3
def roman_to_int(roman_string):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    yosephres = 0
    yosephp = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if val[roman_string[c]] >= yosephp:
                yosephres += val[roman_string[c]]
            else:
                yosephres -= val[roman_string[c]]
            yosephp = val[roman_string[c]]
    return yosephres
