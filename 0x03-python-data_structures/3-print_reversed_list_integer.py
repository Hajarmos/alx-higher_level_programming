#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        rev = my_list[len(my_list) - 1::-1]
        for j in rev:
            print('{:d}'.format(j))
