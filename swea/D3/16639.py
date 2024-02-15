# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZszJXq6s8DFAVw&probBoxId=AY2qdah6_SgDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    furnace = [0] * N  # 용광로 == 화덕 == 큐
    furnace_idx = [0] * N  # 화덕에 있는 피자 인덱스
    melted = [0] * M  # 완성된 피자 저장 인덱스
    count = 0  # 완성된 피자 개수
    furnace_not_full = False
    front = rear = -1

    def bake(furnace):
        global front, count

        # 화덕이 가득 차지 않았다면
        if furnace_not_full:
            # 현재 front는 직전에 0이 돼서 빼낸 피자 위치
            while count < M - 1:
                front = front + 1 if front < N-1 else 0
                furnace[front] //= 2
                if furnace[front] == 0 and melted[furnace_idx[front]] != 1:
                    melted[furnace_idx[front]] = 1
                    count += 1
            for idx, i in enumerate(furnace):
                if i != 0:
                    # 피자 번호는 인덱스+1
                    return furnace_idx[idx] + 1
        else:
            # 굽자
            while furnace[front] != 0:
                front = front + 1 if front < N-1 else 0
                furnace[front] //= 2
        
        # 피자가 구워졌다
        melted[front] = 1
        count += 1

    # enQueue
    for i in range(N):
        rear += 1
        furnace[i] = C[i]
        furnace_idx[i] = rear

    # enQueue 후 남은 피자는 M-N개
    # 구워질 때마다 남은 피자 enQueue
    for _ in range(M-N):
        bake(furnace)
        if rear + 1 < M:
            rear += 1
            furnace[front] = C[rear]
            furnace_idx[front] = rear

    # 더 이상 enQueue 필요 없이 화덕에 남은 것만 deQueue
    furnace_not_full = True
    print(f'#{t} {bake(furnace)}')
 