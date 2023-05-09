#!/usr/bin/python3
for b in range(ord('z'), ord('a')-1, -1):
    print('{:c}'.format(b) if b % 2 == 0 else chr(b-32), end='')
