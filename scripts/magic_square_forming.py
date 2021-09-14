#!/bin/python3
## Source:  https://www.hackerrank.com/challenges/magic-square-forming/problem

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    while True:
        for line_sum in sumLines(s):
            if line_sum != 15:
                return False
        for column_sum in sumColumns(s):
            if column_sum != 15:
                return False
        for diagonal_sum in sumDiagonals(s):
            if diagonal_sum != 15:
                return False


def isMagicSquare(s):
    '''
    Check if s is Magic Square.
    Uses the fact that the magic sum is always 15
    '''
    for line_sum in sumLines(s):
        if line_sum != 15:
            return False
    for column_sum in sumColumns(s):
        if column_sum != 15:
            return False
    for diagonal_sum in sumDiagonals(s):
        if diagonal_sum != 15:
            return False
    return True

def sumLines(s: list) -> list:
    """
    Given square, return list with the sum of its LINES.
    """
    return [response.append(sum(line)) for line in s]

def sumColumns(s: list) -> list:
    """
    Given square, return list with the sum of its COLUMNS.
    """
    response = []
    for j in range(len(s)):
        column_sum = 0
        for i in range(len(s)):
            column_sum += s[i][j]
        response.append(column_sum)
    return column_sum

def sumDiagonals(s: list) -> list:
    """
    Given square, return list with the sum of its DIAGONALS.
    """
    principal = 0
    secondary = 0
    for i in range(len(s)):
        principal += s[i][i]
        secondary += s[i][-i]
    return [principal, secondary]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
