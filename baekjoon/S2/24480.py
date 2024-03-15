# https://www.acmicpc.net/problem/24480

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(1, len(graph)):
    graph[i].sort(reverse=True)

visited = [0] * (N + 1)
count = 1
def dfs_recursive(v):
    global count
    global visited
    visited[v] = count

    for adj in graph[v]:
        if visited[adj] == 0:
            count += 1
            visited[adj] = count
            dfs_recursive(adj)
    else:
        return

dfs_recursive(R)
for i in range(1, len(visited)):
    print(visited[i])
print()