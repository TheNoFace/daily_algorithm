# https://www.acmicpc.net/status?problem_id=1918&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/1918.txt', 'r')
input = sys.stdin.readline

T = int(input().rstrip())

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

for t in range(1, T+1):
    infix = input().rstrip()

    stack = []
    postfix = ''

    for token in infix:
        # 피연산자라면
        if token not in '()*/+-':
            postfix += token
        # 연산자라면
        else: 
            # 닫는 괄호라면 여는 괄호가 나올때까지 pop하여 postfix에 붙임
            if token == ')':
                while stack:
                    c = stack.pop()
                    # 여는 괄호라면 break
                    if c == '(':
                        break
                    postfix += c
            # 닫는 괄호가 아니라면
            else:
                # 스택이 비어있지 않고 현재 연산자의 우선순위가 스택 top의 연산자보다
                # 작거나 같으면 스택 top 원소를 pop하여 postfix에 붙임
                while stack and icp[token] <= isp[stack[-1]]:
                    postfix += stack.pop()
                # 스택이 비어있거나 현재 연산자의 우선순위가 더 높다면
                stack.append(token)
    
    while stack:
        postfix += stack.pop()
    print(postfix)