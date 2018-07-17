#!/usr/bin/env python3


def merge(a, b):

    a_idx = 0
    b_idx = 0

    new = []

    while True:

        if a[a_idx] < b[b_idx]:
            new.append(a[a_idx])
            a_idx += 1
        elif b[b_idx] < a[a_idx]:
            new.append(b[b_idx])
            b_idx += 1
        else:
            new.append(a[a_idx])
            new.append(b[b_idx])
            a_idx += 1
            b_idx += 1

        if a_idx == len(a):
            new.extend(b[b_idx:])
            break
        elif b_idx == len(b):
            new.extend(a[a_idx:])
            break

    return new


def merge_sort(array):

    if len(array) <= 1:
        return array

    middle = len(array) // 2
    a = merge_sort(array[:middle])
    b = merge_sort(array[middle:])
    return merge(a, b)
