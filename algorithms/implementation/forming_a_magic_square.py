#!/bin/python3

import math
import os
import random
import re
import sys


def create_odd_magic_square(n):
    square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    total_count = n ** 2

    i = 0
    j = n // 2
    for num in range(1, total_count + 1):
        square[i][j] = num

        next_i = (i - 1 + n) % n
        next_j = (j + 1) % n

        if square[next_i][next_j]:
            next_i = (i + 1) % n
            next_j = j

        i = next_i
        j = next_j

    return square


def reflect_x(original):
    square = list()
    for i in range(len(original)):
        square.append(original[i][::-1])
    return square


def reflect_y(original):
    return original[::-1]


def rotate_clockwise(original):
    return list(zip(*original[::-1]))


def compute_square_dist(s1, s2):
    n = len(s1)

    total = 0
    for i in range(n):
        for j in range(n):
            total += abs(s1[i][j] - s2[i][j])

    return total


# Complete the formingMagicSquare function below
def formingMagicSquare(s):
    n = len(s)
    # M = n * (n ** 2 + 1) / 2  # magic constant

    squares = [create_odd_magic_square(n)]
    squares.append(reflect_x(squares[-1]))
    squares.append(rotate_clockwise(squares[-1]))
    squares.append(reflect_y(squares[-1]))
    squares.append(rotate_clockwise(squares[-1]))
    squares.append(reflect_x(squares[-1]))
    squares.append(rotate_clockwise(squares[-1]))
    squares.append(reflect_y(squares[-1]))

    return min([compute_square_dist(s, sq) for sq in squares])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
