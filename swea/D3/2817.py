# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # 부분집합의 합
    count = 0
    for i in range(1 << N):
        subset_sum = 0
        for j in range(N):
            if i & (1 << j):
                subset_sum += arr[j]
                if subset_sum > K:
                    break
        if subset_sum == K:
            count += 1

    print(f'#{t} {count}')