# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    chess = [[0] * N for _ in range(N)]
    count = 0
    
    def place_queen(r, n):
        """
           r: 놓을 열 인덱스
           n: 체스판 크기(N)
        """
        global count

        # 종료 조건: 마지막 열까지 퀸을 배치했을 때
        if r == N:
            count += 1
            return
        else:
            """
                1) 같은 열의 윗 행에 퀸이 없다면
                2) 대각선 왼쪽/오른쪽 위에 퀸이 없다면
                3) 퀸 배치 
            """
            for c in range(n):
                # is_placable 변수를 함수 초기에 초기화하면 현재 행에서 배치 불가능한 열이 있을 경우
                # 이후 그 행의 나머지 열의 배치 가부를 검사하지 않고 break
                # 따라서 직전 열의 검사가 break 됐을 때 is_placable 변수 초기화 필요
                is_placable = True
                
                # 1) 같은 열의 윗 행 검사
                # 같은 열에 퀸이 배치되었다면, 0 ~ r-1에 위치
                for i in range(r):
                    if chess[i][c] == 1:
                        is_placable = False
                        break

                # 2) 대각선 좌우 검사
                if is_placable:
                    for i in range(1, r+1):  # 대각선 좌
                        if r-i >= 0 and c-i >= 0 and chess[r-i][c-i] == 1:
                            is_placable = False
                            break
                if is_placable:
                    for i in range(1, r+1):  # 대각선 우
                        if r-i >= 0 and c+i < N and chess[r-i][c+i] == 1:
                            is_placable = False
                            break
                
                # 3) break가 걸리지 않았다면, 퀸 배치
                if is_placable:
                    chess[r][c] = 1
                    place_queen(r+1, n)
                    # 이후 현재 열에 대한 재귀가 끝났다면, 현재 퀸이 놓인 위치 초기화
                    chess[r][c] = 0

    place_queen(0, N)
    print(f'#{t} {count}')
