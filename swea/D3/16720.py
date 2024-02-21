# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZ7-F9qCpwDFAVQ&probBoxId=AY3JQszKcs4DFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        i, n = map(int, input().split())
        tree[i] = n

    # 후위 순회로 접근하며 부모 노드 i가 0이면 자식 노드의 값의 합을 저장
    def postorder_append(i):
        if i <= N:
            left = postorder_append(i*2)
            right = postorder_append(i*2+1)
            if left is None: left = 0
            if right is None: right = 0
            
            if tree[i] == 0:
                tree[i] = left + right
            return tree[i]

    postorder_append(1)
    print(f'#{t} {tree[L]}')