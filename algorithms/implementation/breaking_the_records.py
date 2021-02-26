#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    mn = scores[0]
    mx = scores[0]
    mn_count = 0
    mx_count = 0

    for s in scores[1:]:
        if s < mn:
            mn_count += 1
            mn = s
        elif s > mx:
            mx_count += 1
            mx = s

    return mx_count, mn_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
