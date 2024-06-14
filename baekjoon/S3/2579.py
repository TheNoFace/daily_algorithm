# https://www.acmicpc.net/problem/2579

## Referenced
# https://sungmin-joo.tistory.com/18

import sys

input = sys.stdin.readline

N = int(input())

stairs = []
for _ in range(N):
    stairs.append(int(input()))

dp = [0] * N

"""
현재 위치가 i일 때 가능한 조합
1. (i - 1)에서 왔을 경우: (i - 2)을 밟고 오면 안됨, 따라서 (i - 3)에서 시작
2. (i - 2)에서 왔을 경우: 직전에 어떤 것을 밟았든지 상관 없음
"""

# 초기값 설정
dp[0] = stairs[0]

if N >= 2:
    dp[1] = max(stairs[0] + stairs[1], stairs[1])
    if N >= 3:
        dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

        for i in range(3, N):
            dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[-1])
