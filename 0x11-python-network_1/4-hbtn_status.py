#!/usr/bin/python3
"""Fetching Data Using requests package"""

import requests

if __name__ == "__main__":
    R = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(R.text)}")
    print(f"\t- content: {R.text}")
