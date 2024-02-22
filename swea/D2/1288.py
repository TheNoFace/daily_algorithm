# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18_yw6I9MCFAZN

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = []

    k = 1
    while len(nums) < 10:
        num = N * k
        for i in range(len(str(num))):
            if str(num)[i] not in nums:
                nums.append(str(num)[i])
        k += 1

    print(f'#{t} {N*(k-1)}')
