# https://www.acmicpc.net/problem/24479
# https://www.acmicpc.net/board/view/129242

import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(v):
    stack = []
    visited = [0] * (N + 1)
    count = 1
    visited[v] = count
    
    while True:
        for adj in sorted(graph[v]):
            if visited[adj] == 0:
                stack.append(v)
                stack.append(adj)
                count += 1
                visited[adj] = count
                v = adj
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return visited

for i in dfs(R)[1:]:
    print(i)