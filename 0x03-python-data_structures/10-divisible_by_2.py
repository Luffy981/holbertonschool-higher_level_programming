#!/usr/bin/python3
def divisible_by_2(my_list=[]):
	lista = []
	for i in my_list:
		if i % 2 == 0:
			lista = lista.append(True)
		else:
			lista = lista.append(False)
	return lista
