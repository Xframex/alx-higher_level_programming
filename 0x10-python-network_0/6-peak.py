#!/usr/bin/python3
"""Function that finds a peak on an unsorted array"""


def find_peak(list_of_integers):
    """finds a peak on an unsorted array"""
    li = list_of_integers
    size = len(li)
    middle = int(size / 2)
    if size == 0:
        return
    if (middle == size - 1 or li[middle] > li[middle + 1])\
       and (li[middle] > li[middle - 1] or middle == 0):
        return li[middle]

    if middle != size - 1 and li[middle + 1] > li[middle]:
        return find_peak(li[middle + 1:])
    return find_peak(li[:middle])
