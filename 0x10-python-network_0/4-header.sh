#!/bin/bash
# script that sends a GET request of a given URL with a header variable
curl -sH "X-School-User-Id: 98" "$1"
