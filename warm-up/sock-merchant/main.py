#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    colors = set()
    for val in ar: 
        if not val in colors:
            colors.add(val)
        else:
            pairs +=1
            colors.remove(val)
    return pairs

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


