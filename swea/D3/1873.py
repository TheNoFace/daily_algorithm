# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LyE7KD2ADFAXc

import sys
import os
from pprint import pprint
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

"""
.	평지(전차가 들어갈 수 있다.)
*	벽돌로 만들어진 벽
#	강철로 만들어진 벽
-	물(전차는 들어갈 수 없다.)
^	위쪽을 바라보는 전차(아래는 평지이다.)
v	아래쪽을 바라보는 전차(아래는 평지이다.)
<	왼쪽을 바라보는 전차(아래는 평지이다.)
>	오른쪽을 바라보는 전차(아래는 평지이다.)

U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

* 전차는 맵 밖으로 이동할 수 없음

* 포탄은 벽에 충돌하거나 게임 맵 밖으로 나갈 때까지 직진
* 포탄이 벽에 부딪힐 때
  - 부딪힌 벽이 벽돌로 만들어진 벽이라면, 평지로 바뀜
  - 부딪힌 벽이 벽돌로 만들어진 강철이면, 포탄만 소멸
* 게임 맵 밖으로 포탄이 나가면 포탄은 소멸
"""

T = int(input())

for t in range(1, T+1):
    global battlefield, height, width, N
    height, width = map(int, input().split())
    battlefield = [list(input().rstrip()) for _ in range(height)]
    N = int(input())
    user_input = list(input())

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 탱크/포탄이 향하는 방향
    dh = ['^', 'v', '<', '>']

    # 현재 위치, 방향 반환
    def find_tank(arr):
        direction = ['^', 'v', '<', '>']
        for point in direction:
            count = row = column = 0
            for a in arr:
                if point in a:
                    column = a.index(point)
                    row = count
                    return row, column, point
                else:
                    count += 1

    # 탱크의 위치 이동
    def tank_move(i, r, c, d):
        # print(f'TANK STATUS    : ({r}, {c}) / {battlefield[r][c]}')
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < height and 0 <= nc < width and battlefield[nr][nc] == '.':
            # 탱크 방향 설정
            battlefield[nr][nc] = dh[i]
            # 이전 위치 평탄화
            battlefield[r][c] = '.'
            # 위치, 방향 반환
            # print(f'TANK MOVED({dh[i]})  : ({r}, {c}) -> ({nr}, {nc}) / {battlefield[nr][nc]}')
            return nr, nc, dh[i]
        else:
            # print(f'INVALID MOVE({dh[i]}): ({r}, {c}) -> ({nr}, {nc}) / {battlefield[nr][nc]}')
            battlefield[r][c] = dh[i]
            return r, c, dh[i]

    # 포탄 위치 이동
    def round_move(r, c, d):
        # print(f'TANK FIRES     : ({r}, {c}) to {d}')
        i = dh.index(d)
        nr = r
        nc = c

        while True:
            # print(f'ROUND MOVES    : ({nr}, {nc}) -> ({r + dr[i]}, {c + dc[i]})')
            nr = nr + dr[i]
            nc = nc + dc[i]

            # 맵 밖으로 나갈 때
            if 0 > nr or height <= nr or 0 > nc or width <= nc:
                # print(f'ROUND OUT OF MAP')
                return
            # 벽돌 벽에 부딪힐 때
            elif battlefield[nr][nc] == '*':
                # print(f'ROUND MEETS BRICK: ({nr}, {nc})')
                battlefield[nr][nc] = '.'
                return
            # 강철 벽에 부딪힐 때
            elif battlefield[nr][nc] == '#':
                # print(f'ROUND MEETS METAL: ({nr}, {nc})')
                # 반복 종료
                return

    # 위치 및 방향 초기화
    r, c, d = find_tank(battlefield)

    for button in user_input:
        battlefield[r][c] = d
        if button == 'U':
            r, c, d = tank_move(0, r, c, d)
        elif button == 'D':
            r, c, d = tank_move(1, r, c, d)
            battlefield[r][c] = d
        elif button == 'L':
            r, c, d = tank_move(2, r, c, d)
            battlefield[r][c] = d
        elif button == 'R':
            r, c, d = tank_move(3, r, c, d)
            battlefield[r][c] = d
        else:  # S
            round_move(r, c, d)
    
    print(f'#{t} ', end='')
    for i in battlefield:
        print(''.join(char for char in i))
