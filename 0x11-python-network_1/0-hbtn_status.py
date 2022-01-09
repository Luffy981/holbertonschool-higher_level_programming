#!/usr/bin/python3
# Python script that fetches https://intranet.hbtn.io/status
#
from urllib.request import urlopen

actions = [
        ("type", lambda html: type(html)),
        ("content", lambda html: html),
        ("utf8 content", lambda html: html.decode()),
]

if __name__ == "__main__":
    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        for header, fun in actions:
            print("\t- {}: {}".format(header, fun(html)))
