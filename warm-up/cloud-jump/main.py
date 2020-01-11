#!/bin/python3

import unittest


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, n):
    position, moves = 0, 0
    while position < n - 1:
        if position + 2 < n and c[position + 2] != 1:
            position += 1
        moves += 1
        position += 1
    return moves

    #    if position + 2 < n and c[position + 2] == 1:


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0], 7), 4)


if __name__ == "__main__":
    unittest.main()