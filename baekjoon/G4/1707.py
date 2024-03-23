# https://www.acmicpc.net/problem/1707
# https://www.acmicpc.net/board/view/137749
# https://code-angie.tistory.com/20

import sys
from collections import deque

input = sys.stdin.readline


# BFS 혹은 DFS로 정점 방문처리: 인접 정점과 다른 색(숫자)로 방문 처리
# 방문 처리하며 인접 정점의 색이 현재 정점과 동일하면 이분 그래프가 아님
def check_bipartite(v):
    global result
    global visited

    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        t = q.popleft()
        for adj in adjl[t]:
            if not visited[adj]:
                visited[adj] = 1 if visited[t] == 2 else 2
                q.append(adj)
            elif visited[adj] and visited[adj] == visited[t]:
                result = False
                return
    return


for _ in range(int(input())):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V)]
    result = True

    for _ in range(E):
        u, v = map(int, input().split())
        adjl[u - 1].append(v - 1)
        adjl[v - 1].append(u - 1)

    visited = [0] * V
    for i in range(V):
        if not visited[i]:
            check_bipartite(i)
        if not result:
            break

    if result:
        print("YES")
    else:
        print("NO")
