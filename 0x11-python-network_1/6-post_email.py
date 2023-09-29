#!/usr/bin/python3
"""
Send POST request with email as parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    response = requests.post(url, data=values)
    print(response.text)
