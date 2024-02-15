# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AV14uWl6AF0CFAYD&probBoxId=AY2qdah6_SgDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

for t in range(1, 11):
    input()
    numbers = list(map(int, input().split()))
    front, rear, length = -1, 7, 8
    is_completed = False

    while not is_completed:
        for i in range(1, 6):
            # rear: 현재 큐의 마지막 인덱스
            # front: 마지막으로 제거된 인덱스
            front = front + 1 if front + 1 < length else 0
            rear = rear + 1 if rear + 1 < length else 0
            if numbers[front] - i > 0:
                numbers[rear] = numbers[front] - i
            else:
                numbers[rear] = 0
                is_completed = True
                break

    print(f'#{t}', end=' ')
    for _ in range(length):
        front = front+1 if front+1 < length else 0
        print(numbers[front], end=' ')
    print()