# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

import sys
import os
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

N = 100

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    dest_r = 98  # 사다리타기의 마지막줄은 좌/우 칸이 비어있음
    dest_c = arr[-1].index(2)
    
    nr = dest_r
    nc = dest_c
    is_arrived = False
    is_forwarding = True
    is_turned = False
    is_left = is_right = False

    # i = 0
    while not is_arrived or i >= 99:
        # 그리드 끝 도착
        if nr == 0:
            is_arrived = True
            break
        # print(f'{i}: now @{nr, nc} -> {arr[nr][nc]}')

        # 직전 상태가 회전한 상태인지, 직진한 상태인지 구분해서 방향 설정
        if is_turned:
            # 상, 하
            d = [[-1, 0], [1, 0]]
        else:
            # 우, 좌
            d = [[0, 1], [0, -1]]

        # 좌우 검색
        # 직전에 돌지 않았고
        if not is_turned:
            # TODO: 좌우 분리
            # print(f'{i}: searching l/r')
            nc_l = nc + d[1][1]
            nc_r = nc + d[0][1]
            # 왼쪽칸 가능 시
            if 0 <= nc_l < N:
                if arr[nr][nc_l] == 1:
                    # print(f'{i}: {(nr, nc_l)} is 1, turning left')
                    nc = nc_l
                    is_turned = True
                    is_left = True
                    is_right = False
                    # print(f'{i}: now @{nr, nc} -> {arr[nr][nc]}')
                elif 0 <= nc_r < N and arr[nr][nc_r] == 1:
                    # print(f'{i}: {(nr, nc_r)} is 1, turning right')
                    nc = nc_r
                    is_turned = True
                    is_left = False
                    is_right = True
                    # print(f'{i}: now @{nr, nc} -> {arr[nr][nc]}')
                else:
                    nr -= 1
                    is_turned = False
            # 오른쪽칸 가능 시
            elif 0 <= nc_r < N:
                if arr[nr][nc_r] == 1:
                    # print(f'{i}: {(nr, nc_r)} is 1, turning right')
                    nc = nc_r
                    is_turned = True
                    is_left = False
                    is_right = True
                    # print(f'{i}: now @{nr, nc} -> {arr[nr][nc]}')
                elif 0 <= nc_l < N and arr[nr][nc_l] == 1:
                    # print(f'{i}: {(nr, nc_l)} is 1, turning left')
                    nc = nc_l
                    is_turned = True
                    is_left = True
                    is_right = False
                    # print(f'{i}: now @{nr, nc} -> {arr[nr][nc]}')
                else:
                    nr -= 1
                    is_turned = False
        # 직전에 돌았으면
        elif is_turned:
            # 위칸이 그리드 밖이 아니면
            if 0 <= nr + d[0][0] < N:
                # print(f'{i}: searching up')
                nr_u = nr + d[0][0]
                # 위로 이동
                if arr[nr_u][nc] == 1:
                    # print(f'{i}: {(nr_u, nc)} is 1, going up')
                    nr = nr_u
                    is_turned = False
                    # print(f'{i}: now @{nr, nc} -> {arr[nr][nc]}')
                # 불가능하면 회전
                else:
                    nc = nc - 1 if is_left else nc + 1
        # i += 1
        # time.sleep(0.1)
    
    print(f'#{t} {nc}')
