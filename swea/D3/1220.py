# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = 10
for t in range(1, T+1):
    input()
    grid = [list(map(int, input().split())) for _ in range(100)]

    count = 0
    for c in range(100):
        stack = []
        for r in range(99, -1, -1):
            magnet = grid[r][c]
            # S극(2)일 경우: 스택에 push
            if magnet == 2:
                stack.append(magnet)
            # N극(1)일 경우: 스택이 비어있지 않고 직전 원소가 2라면 count+1 후 push
            elif magnet == 1:
                if stack and stack[-1] == 2:
                    count += 1
                    stack.append(magnet)

    print(f'#{t} {count}')
