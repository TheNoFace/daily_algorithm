# https://www.acmicpc.net/problem/19532

import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

if b == 0:
    x = c // a
    if e != 0:
        y = (f - d * x) // e
    else:
        y = 0
    print(x, y)
else:
    for t in range(1000):
        for i in [1, -1]:
            x = t * i
            if (c - a * x) % b == 0:
                y = (c - a * x) // b

                if (d * x + e * y) == f:
                    print(x, y)
                    break
