# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa&categoryId=AXuARWAqDkQDFARa

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def is_valid(r, c):
        return 0 <= nr < N and 0 <= nc < N

    max_value = 0
    for r in range(N):
        for c in range(N):
            for i in range(0, 8, 4):
                flies = arr[r][c]
                for d in range(i, i+4):
                    nr, nc = r, c
                    for m in range(1, M):
                        nr = r + dr[d] * m
                        nc = c + dc[d] * m
                        if is_valid(nr, nc):
                            flies += arr[nr][nc]
                if flies > max_value:
                    max_value = flies

    print(f'#{t} {max_value}')
