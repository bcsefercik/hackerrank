#!/bin/python3

import math
import os
import random
import re
import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    dist = lcm(len(c), k)
    total_jumps = dist // k

    total_ts = sum([c[i % len(c)] for i in range(0, dist, k)])

    return 100 - total_jumps - 2 * total_ts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
