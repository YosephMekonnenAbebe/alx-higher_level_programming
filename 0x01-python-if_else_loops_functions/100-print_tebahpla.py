#!/usr/bin/python3
yoseph = ""
for dereje in reversed(range(97, 123)):
    if (dereje % 2) == 0:
        yoseph += chr(dereje)
    else:
        yoseph += chr(dereje-32)
print("{}".format(yoseph), end="")
