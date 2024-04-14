# https://www.acmicpc.net/problem/24723

import sys

input = sys.stdin.readline

N = int(input())

result = 1
for i in range(N):
    result *= 2

print(result)