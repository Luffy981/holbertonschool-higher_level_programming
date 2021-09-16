#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_a_dictionary = a_dictionary.copy()
    for k in a_dictionary.keys():
        n_a_dictionary[k] = n_a_dictionary[k] * 2
    return n_a_dictionary
