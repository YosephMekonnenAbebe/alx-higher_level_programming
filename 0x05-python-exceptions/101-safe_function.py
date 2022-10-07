#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        yoseph_r = fct(*args)
        return yoseph_r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
