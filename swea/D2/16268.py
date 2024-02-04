# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYYlGU56XOkDFARc&categoryId=AYYlGU56XOkDFARc

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    pollens = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for r in range(N):
        for c in range(M):
            temp_pollen = 0
            temp_pollen += array[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    temp_pollen += array[nr][nc]
            pollens.append(temp_pollen)
    print(f'#{t} {max(pollens)}')