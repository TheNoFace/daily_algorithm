# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(len(graph)):
    graph[i].sort()

def bfs(v):
    visited = [0] * (N + 1)
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        now = q.popleft()
        print(now, end=" ")
        for adj in graph[now]:
            if not visited[adj]:
                visited[adj] = 1
                q.append(adj)


def dfs(v):
    stack = []
    visited = [0] * (N + 1)
    visited[v] = 1
    print(v, end=" ")
    
    while True:
        for adj in graph[v]:
            if not visited[adj]:
                stack.append(v)
                visited[adj] = 1
                v = adj
                print(adj, end=" ")
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break


dfs(V)
print()
bfs(V)