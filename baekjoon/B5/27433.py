# https://www.acmicpc.net/problem/27433

import sys

input = sys.stdin.readline

N = int(input())


def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(N))
