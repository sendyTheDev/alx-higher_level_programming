#!/usr/bin/python3
"""
Display value of X-Request-Id variable found in the header of a response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    print(response.headers.get("X-Request-Id"))
