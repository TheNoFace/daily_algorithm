# https://www.acmicpc.net/problem/2206

import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

# BFS + DFS
# BFS로 맵을 탐색하며 벽을 만났을 때
# 벽을 부술지 말지를 DFS로 선택
# DFS 진입 시 진입 전 grid 복사 후 사용

N, M = map(int, input().split())
grid = [list(map(str, input().rstrip())) for _ in range(N)]
dist = -1

def pathfinder(r, c, dist_init, grid, visited, breakable):
    global dist

    temp_grid = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp_grid[i][j] = grid[i][j]

    q = deque()
    q.append((r, c))
    visited[r][c] = dist_init

    while q:
        sr, sc = q.popleft()
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = sr + d[0], sc + d[1]
            if nr == N - 1 and nc == M - 1:
                dist = visited[sr][sc] + 1
                return

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                # 벽을 만났을 때
                if temp_grid[nr][nc] == '1':
                    if breakable:
                        # 재귀 진입
                        # 벽 부수기
                        temp_grid[nr][nc] = '0'
                        pathfinder(sr, sc, visited[sr][sc], temp_grid, visited, False)
                        # 벽 돌아가기
                        temp_grid[nr][nc] = '1'
                        continue
                # 벽이 아닐 경우
                else:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[sr][sc] + 1


visited = [[0] * M for _ in range(N)]
pathfinder(0, 0, 1, grid, visited, True)
print(dist)