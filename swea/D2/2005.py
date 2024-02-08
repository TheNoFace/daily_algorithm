# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P0-h6Ak4DFAUq

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())

    # 현재 리스트 i의 원소 번호 j
    # j는 i-1 리스트의 j-1, j+1 합
    pascal = [[1]]
    for i in range(1, N):
        pascal.append([])
        for j in range(i+1):
            if (j-1 < 0) or j >= len(pascal[i-1]):
                # print('INDEX OUT OF RANGE')
                pascal[i].append(1)
            else:
                num = pascal[i-1][j-1] + pascal[i-1][j]
                pascal[i].append(num)

    print(f'#{t}')
    for line in pascal:
        print(*line)

