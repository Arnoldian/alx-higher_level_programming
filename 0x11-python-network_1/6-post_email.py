#!/usr/bin/python3
"""
module displays response from url input/request (w/ email)
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})

    print(req.text)
