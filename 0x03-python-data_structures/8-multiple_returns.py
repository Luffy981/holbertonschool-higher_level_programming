#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    void = None
    if sentence != "":
        void = sentence[0]
    return len_str, void
