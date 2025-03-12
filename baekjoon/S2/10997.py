# https://www.acmicpc.net/problem/10997

import sys

input = sys.stdin.readline


def solution(N):
    row, column = 4 * N - 1, 4 * N - 3
    grid = [[" "] * (column) for _ in range(row)]

    # 좌, 하, 우, 상
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    # 시작 위치, 방향 초기화
    r, c = 0, column - 1
    d = 0

    def is_valid(r, c):
        return 0 <= r < row and 0 <= c < column

    while True:
        grid[r][c] = "*"
        # 현재 방향으로 한 칸 이동한 좌표
        nr, nc = r + dr[d], c + dc[d]
        if is_valid(nr, nc) and grid[nr][nc] == " ":
            # 현재 방향 기준 두 칸 앞의 좌표
            nnr, nnc = r + 2 * dr[d], c + 2 * dc[d]

            # 두 칸 앞이 범위 내이고 벽이면 방향 전환
            if is_valid(nnr, nnc) and grid[nnr][nnc] == "*":
                d = (d + 1) % 4
                nr, nc = r + dr[d], c + dc[d]

                # 종료 조건
                # 두 칸 앞이 범위 내이고 벽이면 종료
                nnr, nnc = r + 2 * dr[d], c + 2 * dc[d]
                if is_valid(nnr, nnc) and grid[nnr][nnc] == "*":
                    break

            # 이외의 경우, 다음 칸 이동
            r, c = nr, nc
        else:
            # 다음 칸으로 이동할 수 없으면 방향 전환
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
            r, c = nr, nc

    return grid


N = int(input())

if N == 1:
    print("*")
else:
    for r in solution(N):
        print("".join(r).rstrip())
