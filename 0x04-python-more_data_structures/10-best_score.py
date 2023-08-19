#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    st = None
    for i in a_dictionary.keys():
        if max < a_dictionary[i]:
            max = a_dictionary[i]
            st = i
    return st
