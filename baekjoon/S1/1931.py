# https://www.acmicpc.net/problem/1931

import sys

input = sys.stdin.readline

N = int(input())
conferences = [list(map(int, input().split())) for _ in range(N)]

# 가장 빨리 끝나는 회의 선택
conferences = sorted(conferences, key=lambda x: (x[1], x[0]))
picks = [conferences[0]]

for i in range(1, N):
    if conferences[i][0] >= picks[-1][1]:
        picks.append(conferences[i])

print(len(picks))
