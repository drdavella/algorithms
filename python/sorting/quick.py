#!/usr/bin/env python3
import numpy as np


def partition(array, pividx):

    pivot_val = array[pividx]
    array[pividx], array[0] = array[0], array[pividx]

    i = 1
    for j in range(1, len(array)):
        if array[j] < pivot_val:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[0], array[i-1] = array[i-1], array[0]
    return i-1


def median_idx(array):

    idx_map = {}
    num = len(array)

    first = array[0]
    idx_map[first] = 0

    mid = array[num//2] if num % 2 == 0 else array[num//2 - 1]
    if num % 2 == 0:
        mid = array[num//2 - 1]
        idx_map[mid] = num//2 - 1
    else:
        mid = array[num//2]
        idx_map[mid] = num//2

    last = array[-1]
    idx_map[last] = len(array) - 1

    return idx_map[sorted([first, mid, last])[1]]


def quicksort(array):
    if len(array) < 2:
        return 0

    a = 0
    b = 0

    pividx = median_idx(array)
    pividx = partition(array, pividx)
    if pividx < len(array):
        a = quicksort(array[:pividx])
        b = quicksort(array[pividx+1:])

    return a + b + len(array) - 1
