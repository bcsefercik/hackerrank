#!/bin/python3

import math
import os
import random
import re
import sys
import functools


def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a


def gcd_list(lst):
    return functools.reduce(gcd, lst)


def lcm(a, b):
    return int(a * b / gcd(a, b))


def lcm_list(lst):
    return functools.reduce(lcm, lst)


def getTotalX(a, b):
    lcm_a = lcm_list(a)
    gcd_b = gcd_list(b)

    lcm_init = lcm_a

    count = 0
    while lcm_a <= gcd_b:
        if not gcd_b % lcm_a:
            count += 1

        lcm_a += lcm_init

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
