# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def pathfinder(sr, sc):
    q = []
    q.append((sr, sc))

    while q:
        size = len(q)
        # 단계별로 순회
        for _ in range(size):
            r, c = q.pop(0)
            # 현재 위치에서 방향 순회
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                # 미로의 최외곽은 벽으로 둘러싸여있으므로 범위 검사는 불필요
                if maze[nr][nc] != "1":
                    if maze[nr][nc] == "3":
                        return 1
                    q.append((nr, nc))
                    maze[r][c] = "1"
    return 0


T = 10
for t in range(1, T + 1):
    input()
    maze = []
    for _ in range(16):
        maze.append(list(input()))
    print(f"#{t} {pathfinder(1, 1)}")
