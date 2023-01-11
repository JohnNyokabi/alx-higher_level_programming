#!/usr/bin/python3
"""Contains a function that creates a python object from JSON file."""
import json


def load_from_json_file(filename):
    """Creates an obj from JSON file
    Args:
        filename: file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
