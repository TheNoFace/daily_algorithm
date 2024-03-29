# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcv8epqK60DFAVa&probBoxId=AY5UrhSaAAIDFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def search(count, pick_sum):
    global result
    if pick_sum >= result:
        return

    if count == N:
        result = min(result, pick_sum)
        return

    # 단계와 인덱스 모두 선택
    for i in range(N):
        if not pick[i]:
            pick[i] = 1
            search(count + 1, pick_sum + grid[count][i])
            pick[i] = 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = N * 100

    pick = [0] * N
    search(0, 0)
    print(f"#{t}", result)
