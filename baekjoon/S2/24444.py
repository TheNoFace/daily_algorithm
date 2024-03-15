# https://www.acmicpc.net/problem/24444

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
    graph[i].sort()

visited = [0] * (N + 1)
count = 1
def bfs(v):
    global visited
    global count

    q = deque()
    q.append(v)
    visited[v] = count

    while q:
        now = q.popleft()
        for adj in graph[now]:
            if not visited[adj]:
                count += 1
                visited[adj] = count
                q.append(adj)

bfs(R)

for i in range(1, len(visited)):
    print(visited[i])
