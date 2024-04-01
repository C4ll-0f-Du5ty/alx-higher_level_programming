#!/usr/bin/python3
"""takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

import sys
from urllib import parse, request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = parse.urlencode(value).encode('ascii')

    req = request.Request(url, data)
    with request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
