#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n = 1
    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) < 3:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    for arg in argv[1:]:
        print("{:d}: {:s}".format(n, arg))
        n += 1
