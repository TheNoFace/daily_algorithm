# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZ79olqCl8DFAVQ&probBoxId=AY3JQszKcs4DFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 이진 최소힙
    heap = [0] * (N+1)
    last = 0  # 힙의 마지막 노드 번호

    def heap_append(n):
        """
            마지막 노드에 입력값 저장
            저장된 입력 값이 부모 노드보다 작다면 부모 노드와 교환
            루트 노드까지 진행
        """
        global last
        last += 1
        heap[last] = n
        c = last
        p = c // 2

        while p and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            # 기존 부모 노드를 새 자식 노드로 설정
            c = p
            p = c // 2

    for i in arr:
        heap_append(i)

    p = last // 2
    anc_sum = 0
    while p:
        anc_sum += heap[p]
        last = p
        p = last // 2

    print(f'#{t} {anc_sum}')
