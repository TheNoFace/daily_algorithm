# https://www.acmicpc.net/problem/2573

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def glacier_breaker():
    to_break = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    glaciers = 0

    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < M

    def glacier_counter(r, c):
        q = deque()
        q.append((r, c))
        visited[r][c] = 1

        while q:
            sr, sc = q.popleft()
            for i in range(4):
                nr, nc = sr + d[i][0], sc + d[i][1]
                if is_valid(nr, nc):
                    if grid[nr][nc] == 0:
                        to_break[sr][sc] += 1

                    if grid[nr][nc] and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = 1
        return 1

    for r in range(N):
        for c in range(M):
            if grid[r][c] and not visited[r][c]:
                glaciers += glacier_counter(r, c)

    if glaciers == 0:
        return 0
    elif glaciers > 1:
        return glaciers
    else:
        for r in range(N):
            for c in range(M):
                if grid[r][c]:
                    if grid[r][c] < to_break[r][c]:
                        grid[r][c] = 0
                    else:
                        grid[r][c] -= to_break[r][c]
        return -1


count = 0
while True:
    result = glacier_breaker()
    if result == -1:
        count += 1
    else:
        if result == 0:
            count = 0
        break

print(count)
