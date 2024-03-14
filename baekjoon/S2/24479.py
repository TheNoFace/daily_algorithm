# https://www.acmicpc.net/problem/24479
# https://www.acmicpc.net/board/view/129242

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in range(len(graph)):
    graph[i].sort()

def dfs_recursive(v, visited, count):
    if not visited[v]:
        visited[v] = count

    for adj in graph[v]:
        if visited[adj] == 0:
            count += 1
            visited[adj] = count
            count, visited = dfs_recursive(adj, visited, count)

    return count, visited

visited = [0] * (N + 1)
for idx, i in enumerate(dfs_recursive(R, visited, 1)[1]):
    if idx == 0:
        continue
    print(i)
print()