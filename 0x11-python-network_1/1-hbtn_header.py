#!/usr/bin/python3
"""Module that takes in URL, sends a request and
displays the value of X-Request-Id variables
found in the header of the response """
import sys
import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id))
