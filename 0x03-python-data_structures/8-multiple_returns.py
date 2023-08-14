#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    con = 0
    for i in sentence:
        con += 1
    return (con, sentence[:1])
