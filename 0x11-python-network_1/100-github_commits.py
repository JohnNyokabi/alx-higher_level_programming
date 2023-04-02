#!/usr/bin/python3
"""List the most recent commits on github repository"""
import sys
import requests


if __name__ == '__main__':
    repository_name = sys.argv[1]
    userName = sys.argv[2]
    req = requests.get(
          'https://api.github.com/repos/{:}/{:}/commits'.format(
              userName, repository_name)).json()
    if len(req) > 10:
        limit = 10
    else:
        limit = len(req)
    for i in range(limit):
        print("{:}: {:}".format(req[i].get('sha'), req[i].get(
            'commit').get('author').get('name')))
