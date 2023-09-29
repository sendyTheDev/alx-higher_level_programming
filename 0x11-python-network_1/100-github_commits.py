#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of the repository “rails” by
    the user “rails”
"""
import sys
import requests


if __name__ == "__main__":
    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(repo_owner,
                                                              repo_name)

    response = requests.get(url)

    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
