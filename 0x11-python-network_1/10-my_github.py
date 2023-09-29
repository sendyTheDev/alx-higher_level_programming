#!/usr/bin/python3
"""
Display value of X-Request-Id variable found in the header of a response
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    access_token = sys.argv[2]

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(access_token)
    }

    response = requests.get(url, headers=headers)
    print(response.json().get("id"))
