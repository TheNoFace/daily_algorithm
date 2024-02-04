# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXAerAPaVXMDFARP&categoryId=AXAerAPaVXMDFARP

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    pops = []
    for r in range(N):
        for c in range(M):
            # 최대 터트릴 수 있는 거리
            pop_limit = array[r][c]
            # print(f'Now: ({r}, {c}), limit: {pop_limit} / {pops}')
            # 터진 풍선의 꽃가루 합
            temp_pop = 0
            temp_pop += pop_limit
            # 네 방향으로 순회
            for i in range(4):
                for j in range(1, pop_limit+1):
                    nr = r + (j * dr[i])
                    nc = c + (j * dc[i])
                    if 0 <= nr < N and 0 <= nc < M:
                        # print(f'appending ({nr}, {nc}): {array[nr][nc]}')
                        temp_pop += array[nr][nc]
            pops.append(temp_pop)
    
    print(f'#{t} {max(pops)}')

