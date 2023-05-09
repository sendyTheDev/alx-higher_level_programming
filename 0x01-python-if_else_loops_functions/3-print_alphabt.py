#!/usr/bin/python3
for d in range(ord('a'), ord('z')+1):
    if d is not (ord('q')) and d is not (ord('e')):
        print('{}'.format(chr(d)), end='')
