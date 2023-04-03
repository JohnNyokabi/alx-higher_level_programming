#!/usr/bin/python3
"""takes in URL, sends request and displays the value of X-Request-Id"""
import requests
import sys


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
