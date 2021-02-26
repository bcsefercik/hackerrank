#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year, target=256):
    is_leap = False

    if year < 1918:
        if year % 4 == 0:
            is_leap = True
    elif year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            is_leap = True

    lengths = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    count = 0 if not is_leap else 1

    if year == 1918:
        count -= 13

    month = 0
    day = 0

    for i in range(1, 13):
        count += lengths[i]

        if count >= target:
            day = lengths[i] - (count - target)
            month = i
            break

    return f"{str(day).rjust(2, '0')}.{str(month).rjust(2, '0')}.{year}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
