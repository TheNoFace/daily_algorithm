# https://www.acmicpc.net/problem/17952

import sys

input = sys.stdin.readline

N = int(input())

task_stack = []
score = 0

for _ in range(N):
    task = list(map(int, input().split()))
    if task[0] == 1:
        A, T = task[1], task[2]
        if (T - 1) == 0:
            score += A
        else:
            task_stack.append([A, T - 1])
    else:
        if task_stack:
            A, T = task_stack.pop()
            if (T - 1) == 0:
                score += A
            else:
                task_stack.append([A, T - 1])

print(score)
