#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    return_str = ""
    if s[:2] == "12" and s[-2:] == "AM":
        return_str = "00" + s[2:-2]
    elif s[-2:] == "PM" and s[:2] != "12":
        new_hour = int(s[:2]) + 12
        return_str = str(new_hour) + s[2:-2]
    else:
        return_str = s[:-2]

    return return_str

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
