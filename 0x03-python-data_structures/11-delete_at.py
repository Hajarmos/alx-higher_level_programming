#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_listt = my_list[:idx]
    if idx < len(my_list) - 1:
        my_listt = my_listt + my_list[idx + 1:]
        my_list = my_listt
    return my_listt
