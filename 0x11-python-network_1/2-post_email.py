#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
"""
from sys import argv
from urllib.request import urlopen, Request
import urllib.parse


if "__name__" == "__main__":
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = Request(argv[1], data)
    with urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
