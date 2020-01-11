#!/bin/python3

import unittest

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
    
