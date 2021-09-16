#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == int(0):
        return 0
    mul = 0
    sum = 0
    for a,b in my_list:
        mul += a*b
        sum += b
    prom = mul / sum
    return prom
