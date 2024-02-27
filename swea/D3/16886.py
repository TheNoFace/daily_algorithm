# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYchCeQq8CUDFAVa&probBoxId=AY3n_XsqsJgDFAUZ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cc = [list(map(int, input().split())) for _ in range(N)]

    # 1~N 숫자의 중복 불가 순열 생성 후 인접 행렬 이용 배터리 소모량 구하기
    path = [0]
    used = [0] * N
    min_usage = 100 * N

    def pathfinder(n, acum_usage):
        global min_usage

        if n == N-1:
            # 경로 완성, 경로의 배터리 소모량 구하기
            # 마지막 목적지 -> 사무실 복귀 소모량 추가
            acum_usage += cc[path[-1]][path[0]]
            if min_usage > acum_usage:
                min_usage = acum_usage
            return
        if min_usage < acum_usage:
            return

        for i in range(1, N):
            if used[i] == 1:
                continue

            used[i] = 1
            path.append(i)
            # 현재 경로까지 누적 사용량 계산
            acum_usage += cc[path[-2]][path[-1]]
            pathfinder(n+1, acum_usage)
            acum_usage -= cc[path[-2]][path[-1]]
            used[i] = 0
            path.pop()

    pathfinder(0, 0)
    print(f'#{t} {min_usage}')
