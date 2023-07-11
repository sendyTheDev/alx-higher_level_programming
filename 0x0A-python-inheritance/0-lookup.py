#!/usr/bin/python3
"""This module attributes and methods of an object."""

def lookup(obj):
    """
    This function excludes built-in attributes and methods
    that start with double underscores (dunder methods).
    """
    return dir(obj)
