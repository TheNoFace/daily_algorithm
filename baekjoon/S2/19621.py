# https://www.acmicpc.net/problem/19621

import sys

input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: x[0])

last_start = max([meeting[0] for meeting in meetings])


def arranger(idx, count):
    count += meetings[idx][2]

    if meetings[idx][1] > last_start:
        result.append(count)

    for i in range(idx + 2, N):
        arranger(i, count)


result = []
for i in range(N):
    arranger(i, 0)

print(max(result))
