# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXO8QBw6Qu4DFAXS

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    lines.sort(key=lambda x: x[0])
    for idx, line in enumerate(lines):
        for i in range(idx+1, N):
            if lines[i][1] < line[1]:
                count += 1

    print(f'#{t} {count}')
