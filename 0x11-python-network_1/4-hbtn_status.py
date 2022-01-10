#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests
actions = [
        ("type", lambda html: type(html)),
        ("content", lambda html: html),
    ]
response = requests.get("https://intranet.hbtn.io/status")
response = html = response.read()
print("Body response:")
for header, fun in actions:
    print("\t- {}: {}".format(header, fun(html)))  
