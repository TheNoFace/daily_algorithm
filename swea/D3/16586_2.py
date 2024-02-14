# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZXhGGqgKsDFAVw&probBoxId=AY2lPqk6jykDFAXh

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_value = 100
    selected = [0] * N

    def picker(i, n, subset_sum):
        """
            i: 시작 위치
            n: 열 길이
            subset_sum: 직전 부분집합의 합
        """
        global min_value, selected
        
        if min_value <= subset_sum:
            return
        elif i == n:
            if min_value > subset_sum:
                min_value = subset_sum
            return
        else:
            for j in range(N):
                if not selected[j]:
                    selected[j] = 1
                    picker(i+1, n, subset_sum+grid[i][j])
                    selected[j] = 0

    picker(0, N, 0)
    print(f'#{t} {min_value}')
