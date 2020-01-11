#!/bin/python3

import math
import os
import random
import re
import sys

import unittest
from collections import deque


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n * c_lib
    neighbours = {}
    visited = [False] * n
    connectedComponents = 0
    nodes_per_cluster = {}

    def dfs(i, cluster):
        if not visited[i]:
            nodes_per_cluster[cluster] = (
                nodes_per_cluster.get(cluster, 0) + 1)
            visited[i] = True
            my_neighbours = []
            try:
                my_neighbours = neighbours[i + 1]
            except KeyError as ke:
                pass
            for city_id in my_neighbours:
                if not visited[city_id-1]:
                    dfs(city_id-1, cluster)

    for road in cities:
        neighbours[road[0]] = (
            neighbours.get(road[0], []) + [road[1]])
        neighbours[road[1]] = (
            neighbours.get(road[1], []) + [road[0]])

    for i in range(n):
        if not visited[i]:
            dfs(i, i)
            connectedComponents += 1

    roads = sum(x - 1 for x in nodes_per_cluster.values())
    total = c_road * roads + c_lib * connectedComponents

    return total


class Tests(unittest.TestCase):
    def test1(self):
        cities = [[1, 2], [3, 1], [2, 3]]
        n = 3
        c_lib = 2
        c_road = 1
        self.assertEqual(roadsAndLibraries(
            n, c_lib, c_road, cities),
            4)

    def test2(self):
        cities = [[1, 3], [3, 4], [2, 4], [1, 2], [2, 3], [5, 6]]
        n = 6
        c_lib = 2
        c_road = 5
        self.assertEqual(roadsAndLibraries(
            n, c_lib, c_road, cities),
            12)


if __name__ == "__main__":
    unittest.main()
