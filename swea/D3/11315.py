# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXaSUPYqPYMDFASQ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    grid = [list(map(str, input())) for _ in range(N)]

    """
        트리 과정에 있는 문제이니, 대각선 판단할 때 이진 트리를 이용?
        전위 순회를 통해 좌하/우상 대각선 판단
        후위 순회를 통해 좌상/우하 대각선 판단
    """
    # 상 하 좌 우 우하 좌하
    dr = [-1, 1, 0, 0, 1, 1]
    dc = [0, 0, -1, 1, 1, -1]
 
    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < N and grid[r][c] == 'o'
 
    def five_rc(N):
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 'o':
                    for d in range(6):
                        count = 1
                        for i in range(1, 6):
                            nr, nc = r + dr[d] * i, c + dc[d] * i
                            if is_valid(nr, nc):
                                count += 1
                                if count == 5:
                                    return 'YES'
                            else:
                                break
        return 'NO'
         
    print(f'#{t} {five_rc(N)}')
