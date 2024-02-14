# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

# operator priority
opp = {'+': 0, '*': 1}

for t in range(1, 11):
    input()
    infix = list(input())
    postfix = ''
    stack = []

    for token in infix:
        # 피연산자일 경우
        if token not in '+*':
            postfix += token
        # 연산자일 경우
        else:
            # 현재 연산자가 스택 top의 연산자보다 우선순위가 높을 경우
            # 스택에 push, 그렇지 않을 경우 pop
            while stack and opp[stack[-1]] >= opp[token]:
                postfix += stack.pop()
            stack.append(token)
    # 스택에 남은 연산자 비우기
    while stack:
        postfix += stack.pop()
    
    for token in postfix:
        if token not in '+*':
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            if token == '*':
                result = left * right
            else:
                result = left + right
            stack.append(result)

    print(f'#{t} {result}')
