#!/usr/bin/env python
from argparse import ArgumentParser
from math import log, ceil


def karatsuba(x, y):

    # Set an arbitrary threshold for the base case
    if x < 16 or y < 16:
        return x * y

    x_len = ceil(log(x, 2))
    y_len = ceil(log(y, 2))

    suffix_len = max(x_len//2, y_len//2)

    mask = 1
    for _ in range(suffix_len-1):
        mask <<= 1
        mask |= 1

    a = x >> suffix_len
    b = x & mask
    c = y >> suffix_len
    d = y & mask

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    other_term = karatsuba(a+b, c+d)

    difference = other_term - bd - ac

    ac_shift = ac << suffix_len*2
    difference_shift = difference << suffix_len

    return ac_shift + bd + difference_shift


def main():

    p = ArgumentParser()
    p.add_argument('intval', nargs=2, type=int)
    args = p.parse_args()

    k_result = karatsuba(*args.intval)
    d_result = args.intval[0] * args.intval[1]

    print(f'karatsuba result = {k_result}')
    print(f'direct result    = {d_result}')

    assert k_result == d_result, "Invalid result!"


if __name__ == '__main__':
    main()
