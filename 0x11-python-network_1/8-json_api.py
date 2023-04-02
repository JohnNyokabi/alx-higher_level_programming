#!/usr/bin/python3
"""Sends a POST request to a URL with a given letter"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_dict = req.json()
        if len(json_dict.keys()) > 0:
            print("[{:}] {:}".format(json_dict.get('id'),
                                     json_dict.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
