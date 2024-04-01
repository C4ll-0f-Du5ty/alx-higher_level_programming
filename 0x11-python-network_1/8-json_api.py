#!/usr/bin/python3
""" that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import sys
import requests

if __name__ == "__main__":
    q = "" if len(sys.argv) < 2 else sys.argv[1]

    d = {"q": q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=d)

    try:
        data = r.json()
        if not data:
            print("No result")
        else:
            print(f'[{data.get("id")}] {data.get("name")}')
    except r.json:
        print("Not a valid JSON")
