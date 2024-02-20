# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZ2eJmqQ2IDFAVw&probBoxId=AY3EPOWqJT8DFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    # 부모를 인덱스로 사용
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    parent = [0] * (E+2)
    count = 0

    def preorder(T):
        global count
        if T:
            count += 1
            preorder(left[T])
            preorder(right[T])

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        parent[c] = p

    preorder(N)
    print(f'#{t} {count}')
