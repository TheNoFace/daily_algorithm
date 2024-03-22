# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRQm6qfL0DFAUo

import sys
import os
from collections import deque
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def block_count(grid):
    temp_blocks = 0
    for r in range(H):
        for c in range(W):
            if grid[r][c]:
                temp_blocks += 1
    return min(blocks, temp_blocks)


def drop(grid, count, col):
    global blocks

    # 종료 조건
    # 1. N회 도달
    if count == N:
        blocks = block_count(grid)
        return

    # 2. 현재 열에 남은 벽돌이 없을 경우
    if grid[H - 1][col] == 0:
        blocks = block_count(grid)
        return

    # 배열 복사
    temp_grid = [[0] * W for _ in range(H)]
    for r in range(H):
        for c in range(W):
            temp_grid[r][c] = grid[r][c]

    explode(temp_grid, col)
    for col in range(W):
        drop(temp_grid, count + 1, col)


def explode(grid, col):
    # bfs로 만나는 모든 벽돌의 좌표를 0으로 바꿈
    for i in range(H):
        if grid[i][col] != 0:
            r, c = i, col
            break

    q = deque([(r, c)])
    visited = [[0] * W for _ in range(H)]
    visited[r][c] = 1
    to_break = [(r, c)]

    while q:
        sr, sc = q.popleft()
        span = grid[sr][sc]
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for i in range(span):
                nr, nc = sr + d[0] * i, sc + d[1] * i
                if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and grid[nr][nc]:
                    q.append((nr, nc))
                    to_break.append((nr, nc))
                    visited[nr][nc] = 1

    # 없앨 벽돌 추가 완료, 없애고 그리드 정리
    for r, c in to_break:
        grid[r][c] = 0

    for c in range(W):
        stack = []
        for r in range(H):
            if grid[r][c] != 0:
                stack.append(grid[r][c])
                grid[r][c] = 0

        for r in range(H - 1, H - (len(stack) + 1), -1):
            grid[r][c] = stack.pop()


T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    blocks = W * H

    for col in range(W):
        drop(grid, 0, col)

    print(f"#{t}", blocks)
