# https://www.acmicpc.net/problem/2164

import sys
from collections import deque
input = sys.stdin.readline

cards = list(range(1, int(input()) + 1))
q = deque(cards)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])