# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    plate, N = map(str, input().split())

    max_value = 0
    plate = list(plate)
    N = int(N)
    M = len(plate)
    pick = [[] for _ in range(N+1)]

    # N번 교환해서 만들 수 있는 모든 순열 구하기?
    # 현재 위치 idx, 교환 횟수 K
    def list_to_int(lst):
        result = ''
        for i in lst: 
            result += i
        return result
    
    def permutation(idx, K):
        global max_value

        if K == N:
            score = int(list_to_int(plate))
            if max_value < score:
                max_value = score
            return
        elif idx+1 == M:
            return
        else:
            for j in range(idx+1, M):
                plate[idx], plate[j] = plate[j], plate[idx]
                swaped = list_to_int(plate)
                if swaped not in pick[K+1]:
                    pick[K+1].append(swaped)
                    permutation(idx, K+1)
                plate[j], plate[idx] = plate[idx], plate[j]
            permutation(idx+1, K)

    permutation(0, 0)
    print(f'#{t} {max_value}')
