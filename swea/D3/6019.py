# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWajaTmaZw4DFAWM

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input_6019.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    D, A, B, F = map(int, input().split())

    # diff = D
    # fly_distance = fly_time = distance = time = 0
    # order = 1
    # distance = F * time
    
    # while True:
        # 홀수번 순서: A -> B / 짝수번 순서: B -> A
        # train = A if (order % 2 == 1) else B

        # time = diff / (train + F)
        # fly_time += time

        # distance = F * time
        # fly_distance += distance

        # diff = D - ((A + B) * fly_time)

        # if diff <= 0:
        #     break
        # else:
        #     order += 1

    # 파리의 이동거리 == 기차의 이동거리
    print(f'#{t} {F * (D / (A + B))}')