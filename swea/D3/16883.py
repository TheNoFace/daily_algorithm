# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYchBw8K7-kDFAVa&probBoxId=AY3n_XsqsJgDFAUZ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    sr = sc = 0
    tr = tc = N-1
    
    direction = [(0, 1), (1, 0)]
    min_sum = 100 * N
    path = []

    def pathfinder(r, c, acum_sum):
        global min_sum

        path.append((r, c))
        acum_sum += grid[r][c]

        # 종료 조건
        # 1) 마지막 목적지에 도달했을 때
        if r == tr and c == tc:
            if acum_sum < min_sum:
                min_sum = acum_sum
            return
        # 2) 현재까지의 합이 최소합보다 클 때
        if acum_sum > min_sum:
            return

        for d in direction:
            nr, nc = r + d[0], c + d[1]
            # 다음 이동 좌표가 유효하고 방문한 적 없다면
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in path:
                pathfinder(nr, nc, acum_sum)
                path.pop()

    pathfinder(sr, sc, 0)
    print(f'#{t} {min_sum}')
