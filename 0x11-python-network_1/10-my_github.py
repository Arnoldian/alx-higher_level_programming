#!/usr/bin/python3
"""
Module uses GitHub API to display GitHub ID on credentials input
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authentication = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=authentication)

    print(req.json().get("id"))
