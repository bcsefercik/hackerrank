#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    shared = 5
    liked_total = 0
    for _ in range(n):
        liked = shared // 2
        shared = liked * 3
        liked_total += liked

    return liked_total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
