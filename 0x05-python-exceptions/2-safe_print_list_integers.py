#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list[0:x]:
        try:
            print("{:d}".format(i), end="")
            count += 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return count
