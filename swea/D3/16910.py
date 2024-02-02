# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcllbDqUVgDFASR&probBoxId=AY1nZhR6QB8DFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())

    grids = 0

    for x in range(-N, N+1):
        for y in range(-N, N+1):
            if (x ** 2) + (y ** 2) <= (N ** 2):
                grids += 1

    print(f'#{t} {grids}')