#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

from collections import deque

class Graph:
    def __init__(self, n):
        self.graph = [set() for _ in range(n)]

    def connect(self, x, y):
        self.graph[x].add(y)
        self.graph[y].add(x)

    def find_all_distances(self, start):
        visited = [-1 for _ in self.graph]
        visited[start] = 0
        q = deque([start])
        while q:
            current = q.popleft()
            for val in self.graph[current]:
                if visited[val] == -1:
                    visited[val] = visited[current] + 6
                    q.append(val)
        return ' '.join((str(val) for i, val in enumerate(visited) if i != start))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    print(graph.find_all_distances(s-1))

