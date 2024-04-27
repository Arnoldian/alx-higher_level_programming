#!/usr/bin/python3
"""
Module displays specific component after
url input and request on same url
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
