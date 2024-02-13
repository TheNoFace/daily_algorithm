# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

for t in range(1, 11):
    int(input())
    infix = input()

    postfix = ''
    stack = []

    for token in infix:
        # 피연산자라면
        if token != '+':
            postfix += token
        # 연산자라면
        else:
            # 스택이 비어있지 않다면 pop
            if stack:
                postfix += stack.pop()
            # 다음 연산자 스택에 push
            stack.append(token)

    # 남은 연산자를 postfix에 붙임
    postfix += stack.pop()
    
    for token in postfix:
        if token != '+':
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)

    print(f'#{t} {stack[-1]}')
