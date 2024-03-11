# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

input = sys.stdin.readline

# 앞 뒤 좌 우 위 아래
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
grid = []


def grid_init(grid, init_pos):
    count = 0
    for i in range(N * H):
        row = list(map(int, input().split()))
        for idx, n in enumerate(row):
            if n == 1:
                init_pos.append((i, idx))
                count += 1
            if n == -1:
                count += 1
        if count == N * H * M:
            return 0
        grid.append(row)
    return init_pos


def bfs(grid, init_pos):
    q = deque()
    q.extend(init_pos)

    def is_valid(nr, nc, sr, sc, r_limit):
        if nr == sr + N or nr == sr - N:
            return 0 <= nr < N * H and 0 <= nc < M and grid[nr][nc] == 0
        return r_limit <= nr < r_limit + N and 0 <= nc < M and grid[nr][nc] == 0
            
    while q:
        r, c = q.popleft()
        r_limit = r // N * N
        for d in range(6):
            nr, nc = r + dr[d] + (N * dh[d]), c + dc[d]
            if is_valid(nr, nc, r, c, r_limit):
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))

    for row in grid:
        if 0 in row:
            return -1
    return grid[r][c] - 1


init_pos = grid_init(grid, [])
if init_pos == 0:
    print(0)
else:
    print(bfs(grid, init_pos))
