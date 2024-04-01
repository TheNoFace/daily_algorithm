# https://www.acmicpc.net/problem/1992

import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, list(input().rstrip()))) for _ in range(N)]
result = ""


def compressor(sr, sc, div):
    global result

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
        if init == 0:
            result += "0"
        else:
            result += "1"
    else:
        # 재귀 진입
        result += "("
        for r in range(sr, sr + div, div // 2):
            for c in range(sc, sc + div, div // 2):
                compressor(r, c, div // 2)
        result += ")"

    return


compressor(0, 0, N)
print(result)
