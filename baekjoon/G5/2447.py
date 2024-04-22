# https://www.acmicpc.net/problem/2447

import sys

input = sys.stdin.readline


def patternizer(r_init, c_init, N):
    div = N // 3

    for sr in range(r_init, r_init + N, div):
        for sc in range(c_init, c_init + N, div):
            if sr == r_init + div and sc == c_init + div:
                continue
            if N > 3:
                patternizer(sr, sc, div)
            else:
                arr[sr][sc] = "*"


N = int(input())
arr = [[" "] * N for _ in range(N)]

patternizer(0, 0, N)
for r in range(N):
    print("".join(arr[r]))
