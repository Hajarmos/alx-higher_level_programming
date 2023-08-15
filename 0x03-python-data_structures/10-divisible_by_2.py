#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    tr = [True]
    fa = [False]
    list_t = []
    for i in my_list:
        if i % 2 == 0:
            list_t = list_t + tr
        else:
            list_t = list_t + fa
    return list_t
