#!/usr/bin/python3
"""
module contains the MyList class
"""


class MyList(list):
    """it's a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """it prints sorted list"""
        print(sorted(self))
