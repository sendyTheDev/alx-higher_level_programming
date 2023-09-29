#!/usr/bin/python3
"""
Send POST request with letter as parameter
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = ""

    if len(sys.argv) > 1:
        letter = sys.argv[1]

    response = requests.post(url, data={'q': letter})
    try:
        data = response.json()

        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
