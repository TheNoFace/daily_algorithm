# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

for t in range(1, 11):
    N, nums = input().split()
    stack = []
    for n in nums:
        if stack and stack[-1] == n:
            stack.pop()
        else:
            stack.append(n)
    print(f'#{t} {"".join(stack)}')