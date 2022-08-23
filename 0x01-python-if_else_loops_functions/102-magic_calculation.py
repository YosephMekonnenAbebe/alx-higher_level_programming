#!/usr/bin/python3
def magic_calculation(a, b, c):
    d = a + b
    e = (a * b) - c
    if a < b:
        return c
    if c > b:
        return d
    return e
