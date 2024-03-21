# https://www.acmicpc.net/problem/16928

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

boards = [i for i in range(100)]
path = [0] * 100

for _ in range(N):
    x, y = map(int, input().split())
    boards[x - 1] = y - 1

for _ in range(M):
    u, v = map(int, input().split())
    boards[u - 1] = v - 1


def bfs(v):
    q = deque([v])
    path[v] = 1

    # 주사위를 굴려 이동할 곳이 이전에 방문한 곳이라면 continue
    while q:
        now = q.popleft()
        for i in range(1, 7):
            if now + i >= 100:
                break
            if now + i == 99:
                return path[now]

            to = boards[now + i]
            if not path[to]:
                q.append(to)
                path[to] = path[now] + 1


print(bfs(0))
