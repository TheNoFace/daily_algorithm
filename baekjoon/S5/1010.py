# https://www.acmicpc.net/problem/1010

import sys

input = sys.stdin.readline


def combination(s, e):
    if s < e:
        s, e = e, s

    numerator, denominator = 1, 1
    K = min(abs(s - e), abs(e - s))

    for i in range(K):
        numerator *= s
        s -= 1
    for i in range(K, 0, -1):
        denominator *= i

    return numerator // denominator


T = int(input())
for _ in range(T):
    s, e = map(int, input().split())
    print(combination(s, e))
