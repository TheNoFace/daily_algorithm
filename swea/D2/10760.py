# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXSHJueab1oDFAQT&categoryId=AXSHJueab1oDFAQT

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

T = int(input())
for t in range(1, T + 1):

    N, M = map(int, input().split())
    planet = [list(map(int, input().split())) for _ in range(N)]

    def is_valid(r, c, now):
        return 0 <= r < N and 0 <= c < M and planet[r][c] < now

    promising = 0
    for r in range(N):
        for c in range(M):
            # 가장자리는 3개밖에 확인할 수 없으므로 제외
            if (
                (r == 0 and c == 0)
                or (r == 0 and c == M - 1)
                or (r == N - 1 and c == 0)
                or (r == N - 1 and c == M - 1)
            ):
                continue
            else:
                count = 0
                now = planet[r][c]
                for d in range(8):
                    nr, nc = r + dr[d], c + dc[d]
                    if is_valid(nr, nc, now):
                        count += 1
                if count >= 4:
                    promising += 1

    print(f'#{t} {promising}')
