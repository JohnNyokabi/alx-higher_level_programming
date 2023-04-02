#!/usr/bin/python3
"""Takes in URL, sends a POST request to the URL"""
import requests
import sys


if __name__ == '__main__':
    payload = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=payload)
    print(req.text)
