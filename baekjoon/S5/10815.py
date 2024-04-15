# https://www.acmicpc.net/problem/10815

import sys

input = sys.stdin.readline

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
to_check = list(map(int, input().split()))

for i in to_check:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
