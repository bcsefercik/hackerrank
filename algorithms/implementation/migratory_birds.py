#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    counts = dict()
    for a in arr:
        counts[a] = counts.get(a, 0) + 1

    return max(
        sorted(counts.items(), key=lambda x: x[0]),
        key=lambda x: x[1]
    )[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    if os.environ.get('INPUT_PATH'):
        with open(os.environ['INPUT_PATH']) as fp:
            in1 = fp.readline()
            in2 = fp.readline()
    else:
        in1 = input()
        in2 = input()



    arr_count = int(in1.strip())

    arr = list(map(int, in2.rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
