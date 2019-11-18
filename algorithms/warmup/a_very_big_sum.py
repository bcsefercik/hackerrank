#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    total = ""
    digit_sum = 0
    while True:
        for i, v in enumerate(ar):
            last_digit = v % 10
            digit_sum += last_digit
            ar[i] = math.floor(v/10)

        new_digit = digit_sum % 10
        total = str(new_digit) + total
        digit_sum = math.floor(digit_sum/10)

        if sum(ar) < 1:
            if digit_sum > 0:
                total = str(digit_sum) + total
            break
            
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ar_count = int(input())
    ar_count = 10

    # ar = list(map(int, input().rstrip().split()))
    in2 = "1001458909 1004570889 1007019111 1003302837 1002514638 1006431461 1002575010 1007514041 1007548981 1004402249"
    ar = list(map(int, in2.rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
