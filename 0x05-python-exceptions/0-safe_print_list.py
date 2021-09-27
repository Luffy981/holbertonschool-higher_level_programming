#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if count < x or count > len(my_list):
                print("{:d}".format(int(i)), end="")
            else:
                break
        except ValueError:
            break
        finally:
            print("{:d}".format(count))
        count += 1

