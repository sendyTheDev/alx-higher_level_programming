#!/usr/bin/python3
"""
module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true if obj is the equivalent to class a_class
    otherwise false
    """
    return (type(obj) == a_class)
