# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

import sys
import os
from collections import deque

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def bfs(v):
    q = deque([v])
    visited = [0] * 101
    visited[v] = 1
    max_count = 1
    left = 0

    while q:
        v = q.popleft()
        for adj in adjl[v]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = visited[v] + 1
                if max_count < visited[adj]:
                    max_count = visited[adj]
                    leaf = adj
                elif max_count == visited[adj]:
                    if leaf < adj:
                        leaf = adj
    return leaf


T = 10
for t in range(1, T + 1):
    N, V = map(int, input().split())
    arr = list(map(int, input().split()))
    adjl = [[] for _ in range(101)]

    for i in range(0, N, 2):
        a, b = arr[i], arr[i + 1]
        adjl[a].append(b)

    print(f"#{t}", bfs(V))
