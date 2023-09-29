#!/usr/bin/python3
""" Python script finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):
    """
  Finds a peak in a list of unsorted integers.

  Args:
    list_of_integers: The list of integers to search
    """
    low = 0
  high = len(list_of_integers) - 1

  while low <= high:
    mid = (low + high) // 2

    if list_of_integers[mid - 1] < list_of_integers[mid] and list_of_integers[mid + 1] < list_of_integers[mid]:
      return mid
    elif list_of_integers[mid - 1] > list_of_integers[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return None
