#!/usr/bin/python3
colon = ", "
for yoseph in range(0, 100):
    Last = yoseph % 10
    First = (int(yoseph/10))
    if yoseph < 10 and (Last != First):
        print("{}{}".format(0, yoseph), end=colon)
    if yoseph > 9:
        if (Last == First) or (Last == 0) or (First > Last):
            continue
        else:
            if yoseph == 89:
                colon = "\n"
        print(yoseph, end=colon)
