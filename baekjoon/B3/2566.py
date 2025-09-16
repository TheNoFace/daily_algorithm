# https://www.acmicpc.net/problem/2566

import sys

input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(9)]
max_num, max_r, max_c = 0, 0, 0

for r in range(9):
    for c in range(9):
        if max_num < grid[r][c]:
            max_num = grid[r][c]
            max_r, max_c = r, c

print(max_num)
print(max_r + 1, max_c + 1)
