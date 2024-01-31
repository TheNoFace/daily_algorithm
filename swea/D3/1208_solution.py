# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))
    
    count = [0] * 101
    for i in array:
        count[i] += 1

    # 최고, 최저 인덱스 찾기
    for i in range(1, 101):
        if count[i] != 0:
            min_index = i
            break

    for i in range(100, 0, -1):
        if count[i] != 0:
            max_index = i
            break

    for _ in range(N):
        if (max_index == min_index) or (max_index - min_index) <= 1:
            break

        count[max_index] -= 1
        count[max_index - 1] += 1
        if count[max_index] == 0:
            max_index -= 1

        count[min_index] -= 1
        count[min_index + 1] += 1
        if count[min_index] == 0:
            min_index += 1

    print(f'#{t} {max_index - min_index}')