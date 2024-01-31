# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = 10

for _ in range(1, T+1):
    t = int(input())
    N = 100
    grid = [list(map(int, input().split())) for i in range(N)]
    grid_list = []

    def find_max(*args):
        result = []
        for arg in args:
            max_v = arg[0]
            for num in arg:
                if num > max_v:
                    max_v = num
            result.append(max_v)

        max_v = result[0]
        for num in result:
            if num > max_v:
                max_v = num
        return max_v

    # row
    row_sum = [0] * N
    for r in range(N):
        for c in range(N):
            row_sum[c] += grid[r][c]

    # column
    column_sum = [0] * N
    for c in range(N):
        for r in range(N):
            column_sum[r] += grid[r][c]

    # diagonal
    diag_sum = [0, 0]
    for r in range(N):
        for c in range(N):
            if r == c:
                diag_sum[0] += grid[r][c]
            elif r == N-1-c:
                diag_sum[1] += grid[r][c]

    print(f'#{t} {find_max(row_sum, column_sum, diag_sum)}')