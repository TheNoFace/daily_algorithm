# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]

    rotated = []
    for _ in range(3):
        array = list(zip(*array[::-1]))
        rotated.append(array)

    print(f'#{t}')
    for i in range(N):
        arr = []
        for j in range(3):
            arr.extend(list(rotated[j][i]))
        
        # N개씩 끊어서 출력
        for i in range(0, len(arr), N):
            print(*arr[i:i+N], sep='', end=' ')
        print()
