#!/usr/bin/python3
"""
Display value of X-Request-Id variable found in the header of a response
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        # Get response headers
        header = response.headers

        print(header.get("X-Request-Id"))
