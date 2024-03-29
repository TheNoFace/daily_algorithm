# https://www.acmicpc.net/problem/2630

import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

result = [0, 0]


def search(sr, sc, div):
    if div == 0:
        return

    init = grid[sr][sc]
    count = 0
    for r in range(sr, sr + div):
        for c in range(sc, sc + div):
            if grid[r][c] == init:
                count += 1
            else:
                break
    if count == div**2:
        result[init] += 1
    else:
        # 4분면으로 나누어 재귀 진입
        div //= 2
        search(sr, sc, div)
        search(sr, sc + div, div)
        search(sr + div, sc, div)
        search(sr + div, sc + div, div)
    return


search(0, 0, N)
for i in range(2):
    print(result[i])
