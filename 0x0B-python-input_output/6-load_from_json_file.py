#!/usr/bin/python3
"""function that creates an Object from a “JSON file"""


import json


def load_from_json_file(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        my_object = json.load(f)
    return my_object
