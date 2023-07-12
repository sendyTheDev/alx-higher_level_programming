#!/usr/bin/python3
"""returns the number of characters written"""



def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) """
    with open(filename, mode='w', encoding='utf-8') as f:
        len = f.write(text)

    return len
