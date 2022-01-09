#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
jojo
"""


if "__name__" == "__main__":
    from sys import argv
    from urllib.request import urlopen, Request
    import urllib.parse
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = Request(argv[1], data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
