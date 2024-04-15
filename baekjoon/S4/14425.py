# https://www.acmicpc.net/problem/14425

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

word_set = set()
for _ in range(N):
    word_set.add(input().rstrip())

count = 0
for _ in range(M):
    if input().rstrip() in word_set:
        count += 1

print(count)
