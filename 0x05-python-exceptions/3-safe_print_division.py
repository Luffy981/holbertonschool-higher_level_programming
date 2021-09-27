#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        r = a \ b
    except:
        print("None")
    finally:
        print("{}".format(r))
