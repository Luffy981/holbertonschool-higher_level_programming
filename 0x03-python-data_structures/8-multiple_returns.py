#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        sentence[0] = None
    a = len(sentence)
    b = sentence[0]
    return a, b
