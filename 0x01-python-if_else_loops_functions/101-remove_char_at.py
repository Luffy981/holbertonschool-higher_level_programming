#!/usr/bin/python3
def remove_char_at(str, n):
    dup = ""
    if n > len(str) or n < 0:
        return(str)
    for i in str:
        if i != str[n]:
            dup = dup + i
    return(dup)
