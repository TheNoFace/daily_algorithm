# https://www.acmicpc.net/problem/11478

import sys

input = sys.stdin.readline

char = input().rstrip()
N = len(char)
substrings = set()

for i in range(1, N + 1):
    s, e = 0, i
    while e <= N:
        substrings.add(char[s:e])
        s += 1
        e += 1

print(len(substrings))
