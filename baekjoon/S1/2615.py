# https://www.acmicpc.net/problem/2615

import sys

input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(19)]

# 우, 하, 우하, 우상
d = [(0, 1), (1, 0), (1, 1), (-1, 1)]


def is_valid(r, c):
    return 0 <= r < 19 and 0 <= c < 19


def check_stone(r, c):
    color = grid[r][c]
    for i in range(4):

        # 6목 회피
        # 이전 방향으로 같은 색상의 돌이 있을 경우, 이전에 확인한 돌
        prev_r, prev_c = r - d[i][0], c - d[i][1]
        if is_valid(prev_r, prev_c) and grid[prev_r][prev_c] == color:
            continue

        nr, nc = r + d[i][0], c + d[i][1]
        count = 1

        while True:
            if is_valid(nr, nc) and grid[nr][nc] == color:
                count += 1
                nr += d[i][0]
                nc += d[i][1]
            else:
                break

        if count == 5:
            return color

    return False


has_found = False
result = 0

for r in range(19):
    for c in range(19):
        if not has_found and grid[r][c]:
            check = check_stone(r, c)

            if check:
                has_found = True
                result = check
                stone = (r, c)

print(result)
if has_found:
    print(stone[0] + 1, stone[1] + 1)
