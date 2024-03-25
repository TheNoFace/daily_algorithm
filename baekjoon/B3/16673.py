# https://www.acmicpc.net/problem/16673

import sys

input = sys.stdin.readline

C, K, P = map(int, input().split())
bottles = 0

for n in range(1, C + 1):
    bottles += K * n + P * n**2

print(bottles)
