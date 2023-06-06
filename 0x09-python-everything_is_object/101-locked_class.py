#!/usr/bin/python3
"""
class that prevents dynamic attributes creation
"""


class LockedClass():
    """Class to prevent dynamic attributes creation"""
    __slots__ = ['first_name']

    def __init__(self):
        pass
