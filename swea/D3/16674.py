# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZxj4kKK_wDFAVw&probBoxId=AY2vXl_qwk4DFAXh

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N and maze[r][c] != "1"


def pathfinder(r_init, c_init, N):
    q = []
    q.append((r_init, c_init))
    distance = 0

    while q:
        size = len(q)
        distance += 1
        for _ in range(size):
            r, c = q.pop(0)
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if is_valid(nr, nc):
                    if maze[nr][nc] == "3":
                        return distance - 1
                    q.append((nr, nc))
                    maze[r][c] = "1"
    return 0


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(input()))

    for r in range(N):
        for c in range(N):
            if maze[r][c] == "2":
                r_init = r
                c_init = c

    print(f"#{t} {pathfinder(r_init, c_init, N)}")
