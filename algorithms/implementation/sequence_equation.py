#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the permutationEquation function below.
def permutationEquation(p):
    matches = dict()
    for i, v in enumerate(p):
        matches[v] = i + 1

    return [matches[matches[i+1]] for i, v in enumerate(p)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
