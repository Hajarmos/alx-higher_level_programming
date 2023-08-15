#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        fc = None
    else:
        fc = sentence[:1]
    return (len(sentence), fc)
