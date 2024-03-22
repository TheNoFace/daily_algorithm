# https://www.acmicpc.net/problem/15686

import os
import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
distance = N ** N

stores = []
houses = []
for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            stores.append((r, c))
        if city[r][c] == 1:
            houses.append((r, c))


def placer(city, level, pick):
    global distance

    if pick and len(pick) == M:
        dist_sum = 0
        for hr, hc in houses:
            temp_dist = []
            for i in pick:
                sr, sc = stores[i]
                temp_dist.append(abs(sr - hr) + abs(sc - hc))
            dist_sum += min(temp_dist)
        distance = min(distance, dist_sum)
        return

    if level == len(stores):
        return

    # 재귀 진입
    # 선택
    placer(city, level + 1, pick + [level])
    # 미선택
    placer(city, level + 1, pick)


placer(city, 0, [])
print(distance)
