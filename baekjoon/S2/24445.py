# https://www.acmicpc.net/problem/24445

import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)


count = 1
visited = [0] * (N + 1)
def bfs(v):
    global count
    global visited

    q = deque()
    q.append(v)
    visited[v] = count

    while q:
        now = q.popleft()
        for adj in graph[now]:
            if not visited[adj]:
                q.append(adj)
                count += 1
                visited[adj] = count

bfs(R)

for i in range(1, N + 1):
    print(visited[i])
