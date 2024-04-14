# https://www.acmicpc.net/problem/10872

import sys

input = sys.stdin.readline

N = int(input())

result = 1
while N > 0:
    result *= N
    N -= 1

print(result)
