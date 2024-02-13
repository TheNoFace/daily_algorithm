# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    queens = 0
    count = 0

    # 체스판 그리드를 만들어 퀸은 8, 퀸의 영향권은 1로 표시
    def queen_territory(grid, r, c):
        # 상 하 좌 우 우상 우하 좌하 좌상
        dr = [-1, 1, 0, 0, -1, 1, 1, -1]
        dc = [0, 0, -1, 1, 1, 1, -1, -1]
        r_init, c_init = r, c
        grid[r][c] = 8

        for d in range(8):
            r, c = r_init, c_init
            for i in range(1, N):
                nr = r + dr[d]
                nc = c + dc[d]
                if (0 <= nr < N and 0 <= nc < N) and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    r, c = nr, nc


    def queen_place(chess, r, c):
        # 종료 조건
        if r == N:
            pass

        queen_territory(chess, r, c)
        is_placable = True

        for column in range(N):
            # 1) 같은 c에 1이 존재하는지
            if r - 1 >= 0 and chess[r-1][column]:
                is_placable = False
                break

            # 2) 대각선 검사
            # 2-1) 대각선 왼쪽 위에 1이 있는지
            if r - 1 >= 0 and c - 1 >= 0 and chess[r-1][c-1] == 1:
                is_placable = False
                break

            # 2-2) 대각선 오른쪽 위에 1이 있는지
            if r - 1 >= 0 and c + 1 < N and chess[r-1][c+1] == 1:
                is_placable = False
                break

            # 1~3) 통과하면 퀸 배치 후 다음 row로 이동
            if is_placable:
                queen_territory(chess, r, column)
                queen_place(chess, r+1, 0)

                # 검사 종료 후 다음 c 검사 위해 체스판 초기화?
                chess = [[0] * N for _ in range(N)]