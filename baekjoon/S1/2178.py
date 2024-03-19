# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(str, input().rstrip())) for _ in range(N)]


def pathfinder(r, c):
    q = deque()
    q.append((r, c))
    maze[r][c] = int(maze[r][c])

    while q:
        sr, sc = q.popleft()
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = sr + d[0], sc + d[1]
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == "1":
                if nr == N - 1 and nc == M - 1:
                    return int(maze[sr][sc]) + 1
                q.append((nr, nc))
                maze[nr][nc] = int(maze[sr][sc]) + 1


print(pathfinder(0, 0))
