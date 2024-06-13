# https://www.acmicpc.net/problem/9184

## Referenced
# https://yeoooo.github.io/algorithm/BOJ9148/

import sys

input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 실제 연산이 진행되기 이전에 계산한 값이 있는지 확인
    if memo[a][b][c]:
        return memo[a][b][c]

    if a < b and b < c:
        memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return memo[a][b][c]

    memo[a][b][c] = (
        w(a - 1, b, c)
        + w(a - 1, b - 1, c)
        + w(a - 1, b, c - 1)
        - w(a - 1, b - 1, c - 1)
    )
    return memo[a][b][c]


# 메모이제이션을 위한 3차원 배열 생성
memo = [[[0] * 51 for _ in range(51)] for _ in range(51)]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    else:
        result = w(a, b, c)
        print(f"w({a}, {b}, {c}) = {result}")
