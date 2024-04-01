#!/usr/bin/python3
"""Fetching Info from a url"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as R:
        p = R.read()

    print("Body response:")
    print(f"\t - type: {type(p)}")
    print(f"\t - content: {p}")
    print(f"\t - utf8 content: {p.decode('utf8')}")
