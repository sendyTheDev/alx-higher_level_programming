#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        biggest = my_list[0]
        for n in my_list:
            if n > biggest:
                biggest = n
                return biggest
            else:
                return None
