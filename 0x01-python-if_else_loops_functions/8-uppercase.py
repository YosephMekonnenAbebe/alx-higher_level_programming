#!/usr/bin/python3
def uppercase(str):
    yoseph = ""
    for c in str:
        if ord(c) > 96 and ord(c) < 123:
            yoseph += chr(ord(c)-32)
        else:
            yoseph += c
    print("{}".format(yoseph))
