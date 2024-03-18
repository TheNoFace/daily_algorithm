# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcrVJQaSWgDFAVa&probBoxId=AY5PUAIqnH0DFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    count = 0

    # 좌우 교차로 탐색하며 m에 도달할 때까지 진행
    # 같은 방향 탐색 or m 도달 불가하면 종료
    def binary_search(arr, target, l, r, partition=None):
        global count

        """
            partition: 직전 검색 방향
            1: 왼쪽
            2: 오른쪽
        """
        m = (l + r) // 2

        # 종료 조건
        # 1. 검색 실패
        if l > r:
            return 
        # 2. 검색 성공
        if target == arr[m]:
            count += 1
            return

        if target < arr[m]:
            if partition == 1:
                return
            binary_search(arr, target, l, m - 1, 1)
        elif target > arr[m]:
            if partition == 2:
                return
            binary_search(arr, target, m + 1, r, 2)

    for target in B:
        binary_search(A, target, 0, N - 1)

    print(f'#{t} {count}')