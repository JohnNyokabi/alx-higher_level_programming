#!/usr/bin/python3
"""Module that takes in URL, sends a request and
displays the value of X-Request-Id variables
found in the header of the response """
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get('X-Request-Id'))
