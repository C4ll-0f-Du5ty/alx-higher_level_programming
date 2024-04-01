#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""

import sys
from urllib import error
from urllib import request

url = sys.argv[1]

req = request.Request(url)
try:
    print(request.urlopen(req).read().encode('utf8'))
except error.HTTPError as e:
    print(f"Error code: {e.code}")
