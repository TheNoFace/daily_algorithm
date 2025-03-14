# https://www.acmicpc.net/problem/5972

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())

max_v = int(1e9)
distance = [max_v] * N  # distance[i]: i 노드까지 누적 이동 거리
adjl = [[] for _ in range(N)]

for _ in range(M):
    i, j, cost = map(int, input().split())
    adjl[i - 1].append([cost, j - 1])
    adjl[j - 1].append([cost, i - 1])


def dijkstra(v, N):
    pq = []
    heappush(pq, (0, v))
    distance[v] = 0

    while pq:
        acum_cost, node = heappop(pq)

        # 현재 node를 이전에 더 큰 비용으로 온 적이 있다면
        if distance[node] >= acum_cost:
            for adj in adjl[node]:
                next_cost, next_node = adj

                cost_sum = acum_cost + next_cost

                if distance[next_node] > cost_sum:
                    distance[next_node] = cost_sum
                    heappush(pq, [cost_sum, next_node])


dijkstra(0, N)
print(distance[-1])
