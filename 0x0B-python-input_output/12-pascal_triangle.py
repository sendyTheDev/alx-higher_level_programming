#!/usr/bin/python3
"""function def pascal_triangle(n)"""


def pascal_triangle(n):
    if n <= 0:
        return list()

    tr = []
    for line in range(0, n):
        tmp = []
        for i in range(0, line + 1):
            tmp.append(magic(line, i))
        tr.append(tmp)
    return tr


def magic(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)
    return res
