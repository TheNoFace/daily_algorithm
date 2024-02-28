# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB

import sys
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, list(input()))) for _ in range(N)]
    mid_idx = N // 2
    total_yield = 0

    # 행이 중앙에 도달하기 전까진 범위 증가, 중앙 이후부터는 범위 감소
    i = 0
    for r in range(N):
        for c in range(mid_idx - i, mid_idx + i + 1):
            total_yield += field[r][c]

        if r < mid_idx:
            i += 1
        else:
            i -= 1

    print(f'#{t} {total_yield}')
