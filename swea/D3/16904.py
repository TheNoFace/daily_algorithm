# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYclhsNaNf0DFAVa&probBoxId=AY3tOLq6DUIDFAUZ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    jobs.sort(key=lambda x: x[1])

    # 1. 종료 시간이 가장 빠른 것 선택
    # 2. 이전 종료시간 이후로 시작되는 것 중 종료 시간이 가장 빠른 것 선택

    pick = []
    for i in range(len(jobs)):
        if not pick:
            pick.append(jobs[i])
        else:
            if jobs[i][0] >= pick[-1][1]:
                pick.append(jobs[i])

    print(f'#{t} {len(pick)}')
    