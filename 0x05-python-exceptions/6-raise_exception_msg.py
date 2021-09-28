#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        luffy = "Hola mundo"
        prit(luffy)
    except NameError:
        print(message)
