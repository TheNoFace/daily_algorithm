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
    # 만든 순열 이용한 인덱스 접근을 위해 더미 0 추가
    color_status = {}
    for i in range(N):
        color_status[i] = [0, flag[i].count('W'), flag[i].count('B'), flag[i].count('R')]

    # 완전 탐색
    # 가능한 모든 순열 생성 후 변경 횟수 세기
    # 첫 줄과 마지막 줄은 흰색, 빨간색 고정
    N -= 2
    min_value = M * N
    def perm(idx, pick):
        global min_value
        if idx == N:
            if pick != [1] * N and pick != [3] * N:
                pick_sum = 0
                for i, j in enumerate(pick):
                    pick_sum += M - color_status[i+1][j]
                    if min_value < pick_sum:
                        break
                if min_value > pick_sum:
                    min_value = pick_sum
            return

        for i in range(1, 4):
            if pick:
                # 이번 색상이 직전 색상과 같거나 다음 색상이 아니라면 continue
                if pick[-1] <= i <= pick[-1] + 1:
                    perm(idx+1, pick + [i])
                else:
                    continue
            else:
                perm(idx+1, pick + [i])

    perm(0, [])
    # 첫 줄과 마지막 줄의 교환 횟수 추가
    min_value += (M - color_status[0][1]) + (M - color_status[N+1][3])
    print(f'#{t} {min_value}')
