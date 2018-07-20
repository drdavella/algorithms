#!/usr/bin/env python3


def merge_and_count_split_inversions(left, right):

    i = 0
    j = 0
    inversions = 0
    array = []

    while True:

        # No inversion
        if left[i] < right[j]:
            array.append(left[i])
            i += 1
        elif right[j] < left[i]:
            array.append(right[j])
            j += 1
            inversions += len(left[i:])
        else:
            array.append(left[i])
            array.append(right[j])
            i += 1
            j += 1

        if i == len(left):
            array.extend(right[j:])
            break
        elif j == len(right):
            array.extend(left[i:])
            break

    return array, inversions


def sort_and_count(array):

    if len(array) <= 1:
        return array, 0

    middle = len(array) // 2
    a, x = sort_and_count(array[:middle])
    b, y = sort_and_count(array[middle:])
    c, z = merge_and_count_split_inversions(a, b)

    return c, x + y + z


def count_inversions(array):

    _, num_inversions = sort_and_count(array)
    return num_inversions
