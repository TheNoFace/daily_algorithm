# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_move = 0
    loc = []

    # DFS
    def dfs(sr, sc, count):
        global max_move
        global loc

        for d in [(-1 ,0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = sr + d[0], sc + d[1]
            if 0 <= nr < N and 0 <= nc < N and grid[sr][sc] + 1 == grid[nr][nc]:
                count += 1
                stack.append((sr, sc))
                dfs(nr, nc, count)

        # 네 방향 탐색 종료 후 더 이상 이동 불가능하면 최대값 확인
        if max_move <= count:
            if max_move < count:
                loc.clear()
            max_move = count
            if stack:
                loc.append(grid[stack[0][0]][stack[0][1]])
            else:
                loc.append(grid[sr][sc])
        return

    for r in range(N):
        for c in range(N):
            stack = []
            dfs(r, c, 1)

    print(f'#{t} {min(loc)} {max_move}')
