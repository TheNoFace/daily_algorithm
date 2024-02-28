# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/4408.txt", "r")
# input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # 1) 복도를 나타내는 배열 생성
    # 2) 학생의 방 번호를 복도 배열의 인덱스로 변환
    # 3) 복도배열[시작번호:종료번호+1] += 1
    # 4) 반복 후 배열의 최대값을 구하면 최소 단위 시간

    corridor = [0] * 200
    max_move = 0

    for i in range(N):
        current, target = map(int, input().split())

        # 출발 번호가 도착 번호보다 큰 경우 range가 제대로 작동하지 않기 때문에
        # 오름차순으로 정렬
        if current > target:
            current, target = target, current

        current = current // 2 if current % 2 == 1 else current // 2 - 1
        target = target // 2 if target % 2 == 1 else target // 2 - 1

        for i in range(current, target+1):
            corridor[i] += 1

            if max_move < corridor[i]:
                max_move = corridor[i]

    print(f"#{t} {max_move}")
