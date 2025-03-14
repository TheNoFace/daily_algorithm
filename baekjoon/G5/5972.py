# https://www.acmicpc.net/problem/5972

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

max_v = int(1e9)
distance = [0] * N  # distance[i]: 노드까지 최소 이동 비용
adjm = [[max_v] * N for _ in range(N)]

for _ in range(M):
    i, j, cost = map(int, input().split())
    adjm[i - 1][j - 1] = cost
    adjm[j - 1][i - 1] = cost

for i in range(N):
    adjm[i][i] = 0


def dijkstra(v, N):
    visited = [0] * N
    visited[v] = 1

    # 시작 정점 v과 인접 정점에 대한 비용
    for i in range(N):
        distance[i] = adjm[v][i]

    for _ in range(N):
        min_v = max_v
        u = 0  # 최소 비용으로 갈 수 있는 다음 노드

        for i in range(N):
            if not visited[i] and distance[i] < min_v:
                min_v = distance[i]
                u = i

        visited[u] = 1

        for adj in range(N):
            if 0 <= adjm[u][adj] < max_v:
                # 현재 저장된 가중치와, 현재 노드에서 연결된 노드로 가는 가중치 합 중 최소값
                distance[adj] = min(distance[adj], distance[u] + adjm[u][adj])


dijkstra(0, N)
print(distance[-1])
