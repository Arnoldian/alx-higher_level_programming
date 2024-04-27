#!/usr/bin/python3
"""
Module takes in URL, sends request and displays value
Usage: ./1-hbtn_header.py <URL>
"""
import sys

import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
