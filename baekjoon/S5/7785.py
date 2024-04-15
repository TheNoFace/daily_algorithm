# https://www.acmicpc.net/problem/7785

import sys

input = sys.stdin.readline

N = int(input())

office = set()
for i in range(N):
    name, status = map(str, input().split())
    if status == "enter":
        office.add(name)
    elif status == "leave":
        office.remove(name)

office = list(office)
office.sort(reverse=True)

for i in office:
    print(i)
