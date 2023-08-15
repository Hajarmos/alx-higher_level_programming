#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_empty = ()

    if tuple_a == tuple_empty:
        tuple_a = (0, 0)
    if tuple_b == tuple_empty:
        tuple_b = (0, 0)
    la = len(tuple_a)
    lb = len(tuple_b)
    if la == 1:
        tuple_a = (tuple_a[0], 0)
    if lb == 1:
        tuple_b = (tuple_b[0], 0)

    tup = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tup
