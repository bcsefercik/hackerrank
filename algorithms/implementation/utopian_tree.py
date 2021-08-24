#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the utopianTree function below.
def utopianTree(n):
    h = 1

    for _ in range(n//2):
        h *= 2
        h += 1

    if n and n % 2:
        h *= 2

    return h


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
