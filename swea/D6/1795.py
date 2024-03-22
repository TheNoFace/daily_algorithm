# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4xuqCqBeUDFAUx

import sys
import os
from collections import deque

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def pathfinder(v):
    # v: 시작점
    q = deque([[0, v]])
    # 시작점 거리 초기화
    distance[v][v] = 0

    while q:
        # node: 중간에 거치는 노드
        cumulated_dist, node = q.popleft()

        # 이전에 계산된 node까지의 비용보다 다른 경로를 통해 도달한 node까지의 비용이 더 작다면
        if distance[v][node] >= cumulated_dist:
            for next_dist, next_node in adjl[node]:
                # 다음 위치 이동에 필요한 비용 도출
                dist_sum = cumulated_dist + next_dist

                # 시작점에서 다음 위치로의 이동 비용이 직전에 도출한 비용보다 크다면
                if distance[v][next_node] > dist_sum:
                    # 더 적은 비용으로 이동
                    distance[v][next_node] = dist_sum
                    # 다음 노드 정보와 누적 비용 push
                    q.append((dist_sum, next_node))


T = int(input())
for t in range(1, T + 1):
    N, M, X = map(int, input().split())
    adjl = [[] for _ in range(N)]
    INF = int(100 * 10000)  # C * N

    # 출발 노드 -> X 노드, X 노드 -> 출발 노드 저장할 행렬
    distance = [[INF] * N for i in range(N)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        adjl[x - 1].append((c, y - 1))

    for i in range(N):
        pathfinder(i)

    max_v = 0
    X -= 1
    for i in range(N):
        if i != X:
            dist = distance[X][i] + distance[i][X]
            if max_v < dist:
                max_v = dist

    print(f"#{t}", max_v)
