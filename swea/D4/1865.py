# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

# 이전까지 선택되지 않은 작업을 선택
def dispatcher(jobs, picks, rate_temp):
    """
        jobs: 선택한 작업 개수       
        picks: 지금까지 선택한 작업
        rate_temp: 직전까지의 확률
    """
    global rate

    # 종료 조건
    # 1. N개 작업 선택 완료
    if jobs == N:
        if rate < rate_temp:
            rate = rate_temp
        return
    # 2. 더 낮은 확률
    if rate_temp <= rate:
        return

    for i in range(N):
        if not picks[i] and grid[jobs][i] != 0:
            picks[i] = 1
            dispatcher(jobs + 1, picks, rate_temp * (grid[jobs][i] / 100))
            picks[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    rate = 0
    picks = [0] * N
    
    dispatcher(0, picks, 1)
    print(f"#{t} {rate * 100:.6f}")
