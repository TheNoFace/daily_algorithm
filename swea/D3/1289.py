# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV19AcoKI9sCFAZN

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    target = list(input())
    now = ['0'] * len(target)
    count = 0

    # 현재 모든 비트는 0, target 형태로 바꾸기 위해 필요한 최소 수정 횟수
    # 1. target에서 처음 1이 나온 인덱스부터 모두 변환
    # 2. 다음 인덱스와 현재 상태 비교 후 다르면 상태 변환
    for idx, token in enumerate(target):
        if token != now[idx]:
            count += 1
            for i in range(idx, len(target)):
                now[i] = token

    print(f'#{t} {count}')