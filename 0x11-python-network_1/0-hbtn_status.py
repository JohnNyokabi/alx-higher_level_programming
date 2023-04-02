#!/usr/bin/python3
"""script fetches url status using urllib"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(
            'htts://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {:}".format(type(html)))
        print("\t- content: {:}".format(html))
        print("\t- utf8 content: {:}".format(html.decode('utf-8')))
