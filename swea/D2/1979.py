# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq

import sys
import os
# from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    cross = [list(map(int, input().split())) for _ in range(N)]

    
    # 십자말을 둘러싼 더미 십자말 만들고 안에 집어넣기
    dummy_cross = [[0] * (N+2) for _ in range(N+2)]
    for r in range(1, N+1):
        for c in range(1, N+1):
            dummy_cross[r][c] = cross [r-1][c-1]
    # pprint(dummy_cross)

    count = 0
    fit = [1] * K
    # 행 계산
    for r in range(1, N+1):
        nc = 1
        while nc+K < N+2:
            # print(f'POS: ({r}, {nc}), {dummy_cross[r][nc-1]}, {dummy_cross[r][nc+K]}')
            check = dummy_cross[r][nc:nc+K]
            if check == fit and dummy_cross[r][nc-1] != 1 and dummy_cross[r][nc+K] != 1:
                # print(f'CROSS(R): ({r}, {nc})')
                count += 1
                nc += K
            else:
                nc += 1

    # 열 계산
    for c in range(1, N+1):
        nr = 1
        while nr+K < N+2:
            # print(f'POS: ({nr}, {c}), {dummy_cross[nr-1][c]}, {dummy_cross[nr+K][c]}')
            check = []
            for i in range(nr, nr+K):
                check.append(dummy_cross[i][c])
            
            if check == fit and dummy_cross[nr-1][c] != 1 and dummy_cross[nr+K][c] != 1:
                # print(f'CROSS(C): ({nr}, {c})')
                count += 1
                nr += K
            else:
                nr += 1
    print(f'#{t} {count}')