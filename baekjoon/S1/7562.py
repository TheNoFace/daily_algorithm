# https://www.acmicpc.net/problem/7562

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    L = int(input())
    sr, sc = map(int, input().split())
    tr, tc = map(int, input().split())
    chess = [[0] * L for _ in range(L)]
    chess[sr][sc] = 1
    chess[tr][tc] = "*"

    # 나이트의 이동 가능 방향: 8가지
    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        count = 0

        while q:
            r, c = q.popleft()
            for d in range(8):
                nr, nc = r + dr[d], c + dc[d]
                if nr == tr and nc == tc:
                    return chess[r][c]
                
                if 0 <= nr < L and 0 <= nc < L and not chess[nr][nc]:
                    q.append((nr, nc))
                    chess[nr][nc] = chess[r][c] + 1

    if sr == tr and sc == tc:
        print(0)
    else:
        print(bfs(sr, sc))
