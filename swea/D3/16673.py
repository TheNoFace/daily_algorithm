# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZxjeC6K8IDFAVw&probBoxId=AY2vXl_qwk4DFAXh

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline


def bfs_list(s, g, N):
    q = []
    visited = [0] * (N+1)
    q.append(s)
    visited[s] = 1

    while q:
        now = q.pop(0)
        if now == g:
            return visited[now] - 1
        for adj in adjl[now]:
            if not visited[adj]:
                q.append(adj)
                visited[adj] = visited[now] + 1
    return 0


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adjl = [[] for _ in range(V+1)]
    adjm = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
        adjm[n1][n2] = 1
        adjm[n2][n1] = 1

    S, G = map(int, input().split())
    print(f'#{t} {bfs_list(S, G, V)}')
