# https://www.acmicpc.net/problem/10816

import sys

input = sys.stdin.readline

N = int(input())
cards_input = list(map(int, input().split()))
M = int(input())
check_input = list(map(int, input().split()))

cards = {}
for i in cards_input:
    if cards.get(i):
        cards[i] = cards[i] + 1
    else:
        cards[i] = 1

for i in check_input:
    if cards.get(i):
        print(cards[i], end=" ")
    else:
        print(0, end=" ")
