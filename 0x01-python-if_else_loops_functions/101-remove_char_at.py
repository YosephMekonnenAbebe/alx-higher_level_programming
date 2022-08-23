#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        yoseph = str[:n] + str[n + 1:]
        return (yoseph)
    else:
        return (str)
