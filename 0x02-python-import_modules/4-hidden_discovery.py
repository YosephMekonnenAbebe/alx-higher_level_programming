#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    c = 1;
    for a in dir(hidden_4):
        if c == 1:
            if a[0] != "_" and a[1] != "_":
            print("{}".format(a))
