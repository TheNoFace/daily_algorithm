# https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
R = 1  # 1번 노드에서 출발

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

# 1번 노드에서 도달 가능한 정점 개수
def dfs(v):
    stack = []
    count = 0
    visited = [0] * (N + 1)
    visited[v] = 1

    while True:
        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = 1
                count += 1
                stack.append(v)
                v = adj
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return count

print(dfs(R))
