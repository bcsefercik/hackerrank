#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    num_counts = dict()
    for n in a:
        num_counts[n] = num_counts.get(n, 0) + 1

    len_max = 0
    for i in num_counts:
        len_max = max(
            len_max,
            num_counts.get(i, 0) + num_counts.get(i+1, 0)
        )

    return len_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
