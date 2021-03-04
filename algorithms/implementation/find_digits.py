#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findDigits function below.
def findDigits(n):
    count = 0
    current_n = n

    while current_n > 0:
        digit = current_n % 10

        if digit > 0 and n % digit == 0:
            count += 1

        current_n = current_n // 10

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
