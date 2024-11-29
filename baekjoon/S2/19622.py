# https://www.acmicpc.net/problem/19622

## Referenced
# https://sodehdt-ldkt.tistory.com/147

import sys

input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

# dp[i]: i번째 회의를 고려했을 경우의 최대 인원
dp = [0] * (N + 1)

# DP 배열 초기화
dp[0] = meetings[0][2]

# 직전 회의 혹은 현재 회의 중 최대 인원
dp[1] = max(dp[0], meetings[1][2]) if N > 1 else 0

for i in range(2, N):
    # - 직전 회의를 선택하고, 현재 회의를 선택 X
    # - 직전 회의를 선택하지 않고, 두 번째 전 + 현재 회의 선택
    # 둘 중 인원 수가 많은 것이 현재 회의 i까지 선택했을 때의 최대 인원
    dp[i] = max(dp[i - 1], dp[i - 2] + meetings[i][2])

print(max(dp))
