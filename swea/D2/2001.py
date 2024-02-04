# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    # (r, c) 에서 MxM 행렬 합 구함
    flies = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            # (r, c) 진입, MxM 행렬 추출
            splash = 0
            for mr in range(r, r+M):
                for mc in range(c, c+M):
                    splash += array[mr][mc]
            flies.append(splash)

    print(f'#{t} {max(flies)}')
