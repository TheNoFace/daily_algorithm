# https://www.acmicpc.net/problem/2667

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = [list(map(str, input().rstrip())) for _ in range(N)]

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
zones = []


def bfs(grid, r, c):
    q = deque()
    q.append((r, c))
    # 방문처리
    grid[r][c] = "-1"
    count = 1

    while q:
        sr, sc = q.popleft()
        for d in range(4):
            nr, nc = sr + dr[d], sc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == "1":
                q.append((nr, nc))
                grid[nr][nc] = "-1"
                count += 1
    return count


for r in range(N):
    for c in range(N):
        if grid[r][c] == "1":
            zones.append(bfs(grid, r, c))

print(len(zones))
for i in sorted(zones):
    print(i)
