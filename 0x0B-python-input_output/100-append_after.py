#!/usr/bin/python3
""" function that inserts a line of text to a file,
after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """function
    args:
        filename: file name
        search_string: line befor
        new_string: line to inserte
    """
    with open(filename, 'r') as fi:
        rf = fi.readlines()
    with open(filename, 'w') as f:
        st = ""
        for line in rf:
            st += line
            if search_string in line:
                st += new_string
        f.write(st)
