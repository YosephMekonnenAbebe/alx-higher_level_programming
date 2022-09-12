#!/usr/bin/python3
def magic_calculation(a, b):
    yoseph_result = 0
    for yoseph_i in range(1, 3):
        try:
            if yoseph_i > a:
                raise Exception('Too far')
            yoseph_result += a ** b / yoseph_i
        except Exception:
            yoseph_result = b + a
            break
    return yoseph_result
