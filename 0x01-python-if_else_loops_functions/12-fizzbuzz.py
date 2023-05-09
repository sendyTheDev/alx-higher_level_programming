#!/usr/bin/python3
def fizzbuzz():
    for c in range(1, 100):
        if c % 20 == 0:
            print('FizzBuzz ', end='')
        elif c % 18 == 0:
            print('Fizz ', end='')
        else:
            print('{} '.format(c), end='')
