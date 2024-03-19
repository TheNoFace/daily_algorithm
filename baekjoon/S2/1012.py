# https://www.acmicpc.net/problem/1012

from pprint import pprint
import sys
from collections import deque

input = sys.stdin.readline


def worms(grid, r, c):
    global count

    q = deque()
    q.append((r, c))
    grid[r][c] = -1

    while q:
        sr, sc = q.popleft()
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = sr + d[0], sc + d[1]
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 1:
                q.append((nr, nc))
                grid[nr][nc] = -1


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        c, r = map(int, input().split())
        grid[r][c] = 1

    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                worms(grid, r, c)
                count += 1

    print(count)
