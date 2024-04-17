# https://www.acmicpc.net/problem/1018

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(str, input().rstrip())) for _ in range(N)]
min_count = M * N


def search(sr, sc, grid, count):
    global min_count

    temp_grid = [[0] * 8 for _ in range(8)]
    for r in range(sr, sr + 8):
        for c in range(sc, sc + 8):
            temp_grid[r - sr][c - sc] = grid[r][c]

    for r in range(8):
        if r != 0 and temp_grid[r][0] == temp_grid[r - 1][0]:
            temp_grid[r][0] = "W" if temp_grid[r - 1][0] == "B" else "B"
            count += 1
            if count >= min_count:
                return
        for c in range(1, 8):
            if temp_grid[r][c - 1] == temp_grid[r][c]:
                count += 1
                if count >= min_count:
                    return
                temp_grid[r][c] = "W" if temp_grid[r][c - 1] == "B" else "B"
    min_count = min(min_count, count)


for sr in range(N - 7):
    for sc in range(M - 7):
        # 시작점이 B인 경우와 W인 경우 나눠 두 번 탐색
        search(sr, sc, grid, 0)
        grid[sr][sc] = "W" if grid[sr][sc] == "B" else "B"
        search(sr, sc, grid, 1)

print(min_count)
