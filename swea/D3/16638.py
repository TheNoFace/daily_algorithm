# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZsywzK6q8DFAVw&probBoxId=AY2qdah6_SgDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))

    # front 인덱스만 계속 이동시키면 됨
    front = -1
    for _ in range(M):
        front = front+1 if front < N-1 else 0

    if front+1 > N - 1:
        front = -1

    print(f'#{t} {Q[front+1]}')
