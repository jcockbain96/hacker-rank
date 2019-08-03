#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, n):
    position, moves = 0, 0
    while position < n - 1:
        if position + 2 < n and c[position + 2] != 1:
            position += 1
        moves +=1
        position += 1
    return moves

    #    if position + 2 < n and c[position + 2] == 1:

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()
