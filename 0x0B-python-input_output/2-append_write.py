#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8) """


def append_write(filename="", text=""):
    with open(filename, mode='a', encoding='utf-8') as f:
        len = f.write(text)
    return len
