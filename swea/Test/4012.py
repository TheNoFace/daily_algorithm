# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]

    synergies = [[0] * N for _ in range(N)]
    for r in range(N-1):
        for c in range(r+1, N):
            if r != c:
                synergies[r][c] = foods[r][c] + foods[c][r]

    # 시너지 접근 시 같은 행과 열에 있는 값은 동시 선택 불가
    diff = 40000
    for r in range(N-1):
        for c in range(r+1, N):
            for diff_r in range(N-1):
                for diff_c in range(diff_r+1, N):
                    if diff_r == r or diff_c == c or diff_r == c or diff_c == r:
                        continue
                    else:
                        temp_diff = abs(synergies[r][c] - synergies[diff_r][diff_c])
                        if diff > temp_diff:
                            diff = temp_diff

    print(f'#{t} {diff}')
