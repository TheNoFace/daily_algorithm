# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQmA4uK8ygDFAXj

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    grid = [[0] * (N+2) for _ in range(N+2)]

    # stone init
    mid_idx = N // 2
    grid[mid_idx][mid_idx] = grid[mid_idx+1][mid_idx+1] = 2
    grid[mid_idx][mid_idx+1] = grid[mid_idx+1][mid_idx] = 1
    
    # 상 하 좌 우 우상 우하 좌하 좌상
    dr = [-1, 1, 0, 0, -1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1 ,-1]

    for i in range(M):
        c, r, stone = map(int, input().split())
        grid[r][c] = stone

        for d in range(8):
            to_change = False
            path = []
            k = 1

            while True:
                # 주어진 위치에서 이동 경로를 스택에 저장
                # 그리드 범위 초과시 break 후 path 초기화
                nr, nc = r + dr[d] * k, c + dc[d] * k
                if 1 <= nr < N+1 and 1 <= nc < N+1 and grid[nr][nc] != stone and grid[nr][nc] != 0:
                        path.append((nr, nc))
                        k += 1
                else:
                    # 같은 색을 발견하면 break 후 path 있는 좌표 색 변경
                    if grid[nr][nc] == stone:
                        to_change = True
                    break

            if to_change:
                for target in path:
                    grid[target[0]][target[1]] = stone

    white, black = 0, 0
    for row in grid:
        white += row.count(2)
        black += row.count(1)

    print(f'#{t}', black, white)
