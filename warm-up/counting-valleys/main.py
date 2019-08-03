#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys_traversed = 0
    current_altitude = 0
    for step in s:
        if step == "U":
            current_altitude += 1
            if current_altitude == 0:
                valleys_traversed += 1
        else:
            current_altitude -= 1
    return valleys_traversed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()