#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if type(tuple_a) is tuple and type(tuple_b) is tuple:
        la = len(tuple_a)
        lb = len(tuple_b)
        x = (0,)
        if la > 2 or lb > 2:
            tuple_a = tuple_a[:2]
            tuple_b = tuple_b[:2]
        elif la == 1 or lb == 1:
            if la == 1:
                tuple_a = tuple_a + x
            if lb == 1:
                tuple_b = tuple_b + x
        else:
            if la == 0:
                tuple_a = x + x
            if lb == 0:
                tuple_b = x + x
        tuple_res = [tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]]
        return tuple_res
    else:
        return
