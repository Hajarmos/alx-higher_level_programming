#!/usr/bin/env python3
def pow(a, b):
    if b < 0:
        return a ** b
    if b == 0:
        return 1
    if b == 1:
        return a
    res = a
    for i in range(2, b + 1):
        res = res * a
    return res
