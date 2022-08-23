#!/usr/bin/python3
colon = ", "
for yoseph in range(0, 100):
    if yoseph < 10:
        print(f"{0:d}{yoseph:d}, """, end="")
    else:
        if yoseph == 99:
            colon = "\n"
        print(yoseph, end=colon)
