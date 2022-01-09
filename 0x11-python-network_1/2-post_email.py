#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request
jojo
"""
if "__name__" == "__main__":
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
