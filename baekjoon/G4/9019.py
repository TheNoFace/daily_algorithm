# https://www.acmicpc.net/problem/9019

import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):
    q = deque()
    q.append((v, ""))
    visited = [0] * 10000
    visited[v] = 1

    while q:
        t, cmd = q.popleft()

        for i in "DSLR":
            temp = ""
            if i == "D":
                nt = t * 2 if t * 2 < 10000 else (t * 2) % 10000
                if not visited[nt]:
                    if nt == B:
                        return cmd + i
                    visited[nt] = visited[t] + 1
                    q.append((nt, cmd + i))
            elif i == "S":
                nt = 9999 if t == 0 else t - 1
                if not visited[nt]:
                    if nt == B:
                        return cmd + i
                    visited[nt] = visited[t] + 1
                    q.append((nt, cmd + i))
            elif i == "L":
                nt = t % 1000 * 10 + t // 1000
                if not visited[nt]:
                    if nt == B:
                        return cmd + i
                    visited[nt] = visited[t] + 1
                    q.append((nt, cmd + i))
            elif i == "R":
                nt = t % 10 * 1000 + t // 10
                if not visited[nt]:
                    if nt == B:
                        return cmd + i
                    visited[nt] = visited[t] + 1
                    q.append((nt, cmd + i))


T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print(bfs(A))
