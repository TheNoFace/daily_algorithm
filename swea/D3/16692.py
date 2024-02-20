# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZ2ei8KQ4EDFAVw&probBoxId=AY3EPOWqJT8DFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    def inorder(T):
        global count
        if T:
            inorder(left[T])
            count += 1
            tree[T] = count
            inorder(right[T])

    N = int(input())
    # parent = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    tree = [0] * (N+1)
    count = 0

    # 우선 N개 노드를 갖는 완전 이진 트리를 생성하고
    # 이진 트리의 최하단 노드부터 중위 순회로 접근하며 값 저장
    for p in range(1, N+1):
        if p * 2 <= N:
            left[p] = p * 2
        else:
            break
        if p * 2 + 1 <= N:
            right[p] = p * 2 + 1
        else:
            break

    # # 자식 노드의 루트 인덱스
    # for i in range(1, N+1):
    #     if left[i] != 0:
    #         parent[left[i]] = i
    #     else:
    #         break
    #     if right[i] != 0:
    #         parent[right[i]] = i
    #     else:
    #         break

    inorder(1)
    print(f'#{t} {tree[1]} {tree[N//2]}')
