# https://www.acmicpc.net/problem/4779

import sys

input = sys.stdin.readline


def cantorian(s, e):
    if e - s == 1:
        return

    div = (e - s) // 3

    for i in range(s + div, s + div * 2):
        string[i] = " "

    cantorian(s, s + div)
    cantorian(s + div * 2, e)


inputs = []
while True:
    temp = input().rstrip()

    if temp:
        inputs.append(int(temp))
    else:
        break


for N in inputs:
    string = list("-" * (3**N))
    cantorian(0, 3**N)
    print("".join(string))
