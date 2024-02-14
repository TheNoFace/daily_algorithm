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
    c_idx = [n for n in range(N)]  # grid행의 인덱스

    def picker(i, n):
        """
            i: 시작 위치
            n: 열 길이
            그리드 행의 인덱스를 사용하여 각 행의 숫자로 만들 수 있는 모든 순열 생성
        """
        global min_value
        # 종료 조건
        # 1) 마지막 행에 도달했을 때
        if i == n:
            subset_sum = 0
            for j in range(n):
                # 2) 부분집합의 합이 최소값보다 클 때
                subset_sum += grid[j][c_idx[j]]
                if subset_sum >= min_value:
                    break
            else:
                min_value = subset_sum
            return
        else:
            for j in range(i, n):
                c_idx[i], c_idx[j] = c_idx[j], c_idx[i]
                picker(i+1, n)
                c_idx[j], c_idx[i] = c_idx[i], c_idx[j]

    picker(0, N)
    print(f'#{t} {min_value}')
