# https://www.acmicpc.net/problem/11729

## Referenced
# https://namu.wiki/w/%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98%20%ED%83%91

import sys

input = sys.stdin.readline

N = int(input())
moves = []


def hanoi(N, pole_init, pole_target, pole_thru):

    # 가장 위에 있는 원판을 목표 장대로 옮김
    if N == 1:
        moves.append((pole_init, pole_target))
    else:
        # N 원판을 목표 장대로 옮기기 위해선 N - 1까지의 원판을
        # 목표 장대를 통해 보조 장대로 옮겨야 함
        hanoi(N - 1, pole_init, pole_thru, pole_target)

        # N - 1까지의 원판이 보조 장대로 이동했으므로, N 원판을 목표 장대로 옮김
        moves.append((pole_init, pole_target))

        # 목표 장대에 도착한 N 원판을 제외한 나머지 원판을
        # 현재 위치한 보조 장대에서 시작 장대를 통해 목표 장대로 이동
        hanoi(N - 1, pole_thru, pole_target, pole_init)


hanoi(N, 1, 3, 2)

print(len(moves))
for move in moves:
    print(*move)
