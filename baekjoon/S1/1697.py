# https://www.acmicpc.net/problem/1697

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
time = 0

def operations(n, option):
    if option == 0:
        return n - 1
    elif option == 1:
        return n + 1
    elif option == 2:
        return n * 2

def bfs(v, k):
    global time
    q = deque()
    q.append(v)
    visited = [0] * 100002
    visited[v] = 1

    while q:
        for _ in range(len(q)):
            pos = q.popleft()
            for i in range(3):
                n = operations(pos, i)
                if n == k:
                    return time + 1
                if 0 <= n <= 100000 and not visited[n]:
                    q.append(n)
                    visited[n] = 1
        time += 1

if N == K:
    print(0)
else:
    print(bfs(N, K))