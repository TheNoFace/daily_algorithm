# https://www.acmicpc.net/problem/1764

import sys
sys.stdin = open("input.txt", "r")

N, M  = list(map(int, input().split()))

never_listened = set()
for i in range(N):
    never_listened.add(input())

never_seen = set()
for i in range(M):
    never_seen.add(input())

# set 연산
result = list(never_listened & never_seen)
result.sort()

print(len(result))
[print(i) for i in result]
