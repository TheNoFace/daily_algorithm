# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = 10
for t in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    lc = [0] * (N+1)
    rc = [0] * (N+1)
    parent = [0] * (N+1)

    for _ in range(N):
        inputs = input().split()
        if inputs[1].isdecimal():  # 연산자 X
            tree[int(inputs[0])] = int(inputs[1])
        else:
            tree[int(inputs[0])] = inputs[1]
            lc[int(inputs[0])] = int(inputs[2])
            rc[int(inputs[0])] = int(inputs[3])
            parent[int(inputs[2])] = int(inputs[0])
            parent[int(inputs[3])] = int(inputs[0])

    p = parent[N-1]
    while p >= 1:
        left, right = tree[N-1], tree[N]
        result = eval(f'{left}{tree[p]}{right}')
        # operator = tree[p]
        # if operator == '-':
        #     result = left - right
        # elif operator == '+':
        #     result = left + right
        # elif operator == '*':
        #     result = left * right
        # elif operator == '/':
        #     result = left / right
        tree[p] = result

        N -= 2
        if N <= 1:
            break
        p = parent[N]

    print(f'#{t} {int(result)}')