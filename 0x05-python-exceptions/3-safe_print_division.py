#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        yoseph_result = a / b
    except ZeroDivisionError:
        yoseph_result = None
    finally:
        print("Inside result: {}".format(yoseph_result))
    return yoseph_result
