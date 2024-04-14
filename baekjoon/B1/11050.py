# https://www.acmicpc.net/problem/11050

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

if N > K:
    numerator, denominator = 1, 1
    for i in range(K):
        numerator *= N
        N -= 1
    for i in range(K, 0, -1):
        denominator *= i
    result = numerator // denominator
elif N == K:
    result = 1
else:
    result = 0

print(result)
