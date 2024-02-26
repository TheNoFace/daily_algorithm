# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    result = 'ON'

    # for i in range(N):
    #     if M & (1 << i) == 0:
    #         result = 'OFF'
    #         break

    for i in range(N):
        if M & 0x1 == 0:
            result = 'OFF'
            break
        M = M >> 1

    print(f'#{t} {result}')
