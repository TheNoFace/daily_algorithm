# https://www.acmicpc.net/status?problem_id=12789&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/12789.txt', 'r')
input = sys.stdin.readline

T = 7
for t in range(1, T+1):
    N = int(input().rstrip())
    order = list(map(int, input().split()))

    min_value = 1
    stack = []
    is_sad = False

    """
        우선 스택에 넣고 스택의 top이 min_value인지 확인
        최소값이 아닐경우 계속 스택 push
    """
    for i in order:
        if i == min_value:
            min_value += 1
        else:
            stack.append(i)

        while stack and stack[-1] == min_value:
            stack.pop()
            min_value += 1

    if stack: print('Sad')
    else: print('Nice')
