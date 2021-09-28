#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i, j in zip(my_list_1, my_list_2):
        try:
            res.append(i / j)
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        except TypeError:
            print("wrong type")
            res.append(0)
        finally:
            pass
    if len(my_list_1) != len(my_list_2):
        print("out of range")

    return res
