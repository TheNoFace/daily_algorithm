# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = 10
for t in range(1, T+1):
    def inorder(T):
        if T:
            inorder(left[int(T)])
            print(tree[int(T)], end='')
            inorder(right[int(T)])

    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(1, N+1):
        inputs = input().split()
        if len(inputs) == 4:
            p, tree[i], left[i], right[i] = map(str, inputs)
        elif len(inputs) == 3:
            p, tree[i], left[i] = map(str, inputs)
        else:
            p, tree[i] = map(str, inputs)

    print(f'#{t}', end=' ')
    inorder(1)
    print()
