#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positives = sum(map(lambda x: 1 if x > 0 else 0, arr))
    negatives = sum(map(lambda x: 1 if x < 0 else 0, arr))
    zeros = len(arr) - positives - negatives

    print(positives/len(arr))
    print(negatives/len(arr))
    print(zeros/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
