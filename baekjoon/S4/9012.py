#  https://www.acmicpc.net/problem/9012

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

N = int(input())
pss = [input().rstrip() for _ in range(N)]
good = 0

for test in pss:
    print(test)
    # 3986번과 동일, 스택 사용
    stack = []
    for char in test:
        if stack:
            if char != stack[-1] and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')