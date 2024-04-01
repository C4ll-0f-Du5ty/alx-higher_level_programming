#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable"""

import sys
from urllib import request

with request.urlopen(sys.argv[1]) as res:
    p = res

print(p.headers.get('X-Request-Id'))
