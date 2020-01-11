#!/bin/python3

import math
import os
import random
import re
import sys

import unittest
from collections import deque


def create_adj_matrix(graph_from, graph_to):
    graph = {}
    num_nodes = len(graph_from)
    for i in range(num_nodes):
        if graph_from[i] not in graph:
            graph[graph_from[i]] = [graph_to[i]]
        else:
            graph[graph_from[i]].append(graph_to[i])
        if graph_to[i] not in graph:
            graph[graph_to[i]] = [graph_from[i]]
        else:
            graph[graph_to[i]].append(graph_from[i])
    return graph


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = create_adj_matrix(graph_from, graph_to)
    col_nodes = []

    for j in range(len(ids)):
        if ids[j] == val:
            col_nodes.append(j+1)

    num_target_nodes = len(col_nodes)

    shortest = sys.maxsize
    if num_target_nodes <= 1:
        return -1

    for k in range(num_target_nodes):
        for k2 in range(k+1, num_target_nodes):
            s_path = find_shortest_path_2(graph, col_nodes[k], col_nodes[k2])
            print(s_path)
            if not s_path:
                continue
            if 0 < len(s_path) < shortest:
                shortest = len(s_path) - 1

    if shortest == sys.maxsize:
        return -1
    return shortest


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def find_shortest_path_2(graph, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist.get(end)


class Tests(unittest.TestCase):
    def test1(self):
        graph_nodes = 5
        graph_from = [1, 1, 2, 3]
        graph_to = [2, 3, 4, 5]
        ids = [1, 2, 3, 3, 2]
        val = 2
        self.assertEqual(findShortest(
            graph_nodes, graph_from, graph_to, ids, val), 3)

    def test2(self):
        graph_nodes = 4
        graph_from = [1, 1, 4]
        graph_to = [2, 3, 2]
        ids = [1, 2, 3, 4]
        val = 2
        self.assertEqual(findShortest(
            graph_nodes, graph_from, graph_to, ids, val), -1)

    def test3(self):
        graph_nodes = 4
        graph_from = [1, 1, 4]
        graph_to = [2, 3, 2]
        ids = [1, 2, 1, 1]
        val = 1
        self.assertEqual(findShortest(
            graph_nodes, graph_from, graph_to, ids, val), 1)


if __name__ == "__main__":
    unittest.main()
