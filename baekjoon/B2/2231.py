# https://www.acmicpc.net/problem/2231

import sys

input = sys.stdin.readline


def finder(n, min_N):
    global result

    if min_N >= N:
        return 0

    digit_sum = 0
    i = 10 ** (n - 1)
    temp_N = min_N
    while i > 0:
        digit_sum += temp_N // i
        temp_N %= i
        i //= 10

    if digit_sum + min_N == N:
        return min_N
    else:
        return finder(n, min_N + 1)


N = int(input())

i, n = 1, 0
while N // i:
    i *= 10
    n += 1

min_N = N - (9 * n)
print(finder(n, min_N))
