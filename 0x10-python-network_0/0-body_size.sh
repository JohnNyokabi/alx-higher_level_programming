#!/bin/bash
# Script that takes in URL, sends a request and displays size of the body of response
curl -s $1 --include | grep -i content-length | awk '{print $2}'
