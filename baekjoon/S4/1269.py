# https://www.acmicpc.net/problem/1269

import sys

input = sys.stdin.readline

map(int, input().split())

set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

print(len(set_A.difference(set_B)) + len(set_B.difference(set_A)))
