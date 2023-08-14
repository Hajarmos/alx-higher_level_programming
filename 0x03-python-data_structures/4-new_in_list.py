#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    el = [element]
    new = my_list[:idx] + el
    if idx < len(my_list) - 1:
        new = new + my_list[idx + 1:]
    return new
