#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """function"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
