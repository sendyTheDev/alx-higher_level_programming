#!/usr/bin/python3
for x in range(0, 10):
    for b in range((x+1), 10):
        if (x != 7) or (b != 9):
            print("{}{}, ".format(x, b), end="")
        else:
            print("{}{}".format(x, b))
