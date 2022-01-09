#!/usr/bin/python3
# sends a request to the URL and displays the value of the X-Request-Id

from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as response:
        headers_like_dict = dict(response.getheaders())
        print(headers_like_dict.get('x-Request-Id'))
