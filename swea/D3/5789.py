# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWYygN36Qn8DFAVm

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, Q = map(int, input().split())
    task = [list(map(int, input().split())) for _ in range(Q)]
    box = [0] * N

    for i in range(Q):
        start = task[i][0] - 1
        end = task[i][1]
        # print(start, end)
        for j in range(start, end):
            box[j] = i+1

    print(f'#{t} ', end='')
    print(*box)
    
        


