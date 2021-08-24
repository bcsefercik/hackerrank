#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    return (((m - 1) + (s - 1)) % n) + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    if os.environ.get('INPUT_PATH'):
        ifptr = open(os.environ['INPUT_PATH'])

    t = int(ifptr.readline().strip() if os.environ.get('INPUT_PATH') else input())

    for t_itr in range(t):
        nms = (ifptr.readline().strip() if os.environ.get('INPUT_PATH') else input()).split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()

    if os.environ.get('INPUT_PATH'):
        ifptr.close()
