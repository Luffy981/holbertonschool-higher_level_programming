#!/usr/bin/python3
def print_list_integer(my_list=[]):
	if my_list == []:
		return 0
	for i in my_list:
		print("{:d}".format(i));
