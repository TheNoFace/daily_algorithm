# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
#input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    parenthesis = input()

    stack = []
    cuts = 0
    for idx, p in enumerate(parenthesis):
        if p == ')':
            stack.pop()
            # 직전 괄호가 여는 괄호라면 == 레이저라면
            if parenthesis[idx-1] == '(':
                cuts += len(stack)
            # 아니라면 == 막대기라면
            else:
                cuts += 1
        else:
            stack.append(p)
    print(f'#{t} {cuts}')