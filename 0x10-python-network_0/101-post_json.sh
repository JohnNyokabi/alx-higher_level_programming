#!/bin/bash
# sends a JSON POST request to a URL with a given JSON file
curl -s -H "content-type: application/json" -d "$(cat "$2")" "$1"
