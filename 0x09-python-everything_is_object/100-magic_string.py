#!/usr/bin/python3
def magic_string():
    magic_string.i = getattr(magic_string, 'i', 1) + 1
    print(magic_string.i)
    return ("BestSchool, " * (magic_string.i - 1) + "BestSchool")
