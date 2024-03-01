# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]

    # 색상별 딕셔너리 생성
    # key: row, value: w, b, r의 개수
    color_status = {}
    for i in range(N):
        color_status[i] = [flag[i].count('W'), flag[i].count('B'), flag[i].count('R')]

    # 첫째 줄~(흰색보다 파란색이 더 많은 줄 or N-3번째 줄)까지는 흰색
    sr = nr = 0
    for r in range(sr, N-2):
        if r == sr:
            count = M - color_status[sr][0]
        else:
            if color_status[r][0] >= color_status[r][1]:
                count += M - color_status[r][0]
            else:
                break
        nr += 1

    # (흰색보다 파란색이 더 많은 줄)~(파랑보다 빨강이 더 많은 줄 or N-2번째 줄)까지는 파란색
    sr = nr
    for r in range(sr, N-1):
        if r == sr:
            count += M - color_status[sr][1]
        else:
            if color_status[r][1] >= color_status[r][2]:
                count += M - color_status[r][1]
            else:
                break
        nr += 1

    # 나머지 빨간색
    sr = nr
    for r in range(sr, N):
        count += M - color_status[r][2]

    print(f'#{t} {count}')
