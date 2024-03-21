# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYdJ-ooaDpUDFAVa&probBoxId=AY5evUOan8YDFARi

import sys
import os
from heapq import heappush, heappop

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def pathfinder(v):
    pq = []
    heappush(pq, (0, v))
    distance[v] = 0

    while pq:
        cumulated_dist, pos = heappop(pq)

        # 현재 위치를 이전에 더 많은 비용으로 온 적이 있다면
        if distance[pos] >= cumulated_dist:
            for adj in adjl[pos]:
                next_dist, next_pos = adj

                # 다음 위치 이동에 필요한 누적 비용 도출
                dist_sum = cumulated_dist + next_dist

                # 다음 위치를 도출한 누적 비용보다 더 많은 비용으로 간 적이 있다면
                if distance[next_pos] > dist_sum:
                    # 더 적은 비용으로 이동
                    distance[next_pos] = dist_sum
                    # 다음 이동 정보와 누적 비용 push
                    heappush(pq, (dist_sum, next_pos))
    return distance[N]


inf = int(1e9)
T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    adjl = [[] for _ in range(N + 1)]
    distance = [inf] * (N + 1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        adjl[s].append((w, e))

    print(f"#{t}", pathfinder(0))
