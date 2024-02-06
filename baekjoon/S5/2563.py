# https://www.acmicpc.net/problem/2563

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

count = 0
grid = [[0] * 100 for _ in range(100)]
for paper in papers:
    W, H = paper
    for r in range(H, H+10):
        for c in range(W, W+10):
            if grid[r][c] != 1:
                grid[r][c] = 1
                count += 1

print(count)
