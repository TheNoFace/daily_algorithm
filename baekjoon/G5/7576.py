# https://www.acmicpc.net/problem/7576

import sys
from collections import deque
input = sys.stdin.readline


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
M, N = map(int, input().split())

grid = []
init_pos = []
for i in range(N):
    row = list(map(int, input().split()))
    for idx, n in enumerate(row):
        if n == 1:
            init_pos.append((i, idx))
    grid.append(row)


# 그리드의 0을 모두 1로 바꾸는데 필요한 최소 일수
# BFS의 탐색 방향은 물결로 퍼진다
def bfs(init_pos):
    q = deque()
    q.extend(init_pos)

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0:
                # 방문처리
                grid[nr][nc] = grid[r][c] + 1
                # enqueue
                q.append((nr, nc))

    for row in grid:
        if 0 in row:
            return -1
    return grid[r][c] - 1


print(bfs(init_pos))
