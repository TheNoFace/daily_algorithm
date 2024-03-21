# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYdJ95_aDiADFAVa&probBoxId=AY5evUOan8YDFARi

import sys
import os
from heapq import heappush, heappop

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def prim(v, N):
    pq = []
    visited = [0] * N
    weight_sum = 0
    heappush(pq, (0, v))

    while pq:
        weight, start = heappop(pq)

        # 기존에 이미 더 낮은 가중치로 방문했다면 지나감
        if visited[start]:
            continue

        # 방문 처리
        # 가중치가 가장 작은 것을 방문해야하므로 인접 정점 탐색 시 방문처리하면 안됨
        visited[start] = 1
        weight_sum += weight

        for adj in adjl[start]:
            adj_weight, adj_start = adj[0], adj[1]

            if not visited[adj_start]:
                # print(start, adj_start)
                heappush(pq, (adj_weight, adj_start))

    return weight_sum


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    weight_sum = 0
    adjl = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b, w = map(int, input().split())
        adjl[a].append((w, b))
        adjl[b].append((w, a))

    print(f"#{t}", prim(0, V + 1))
