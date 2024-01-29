# https://www.acmicpc.net/problem/1764

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M  = map(int, input().split())

never_listened = set()
for i in range(N):
    never_listened.add(input().strip())

never_seen = set()
for i in range(M):
    never_seen.add(input().strip())

result = list(never_listened & never_seen)
result.sort()

print(len(result))
[print(i) for i in result]
