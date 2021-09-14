#!/usr/bin/python3
def multiple_returns(sentence):
    len_str = len(sentence)
    void = None
    if sentence is None:
        void = sentence[0]
    return len_str, void
