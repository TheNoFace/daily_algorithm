# https://www.acmicpc.net/problem/1149

## Referenced
# https://hongcoding.tistory.com/123

import sys

input = sys.stdin.readline

N = int(input())

# 메모이제이션
# 각 집이 특정 색상을 선택했을 경우의 누적 비용 저장
dp = [[0] * 3 for _ in range(N)]

houses = []
for i in range(N):
    houses.append(list(map(int, input().split())))

# 첫 번째 집은 모든 색상을 선택 가능
dp[0][0], dp[0][1], dp[0][2] = houses[0][0], houses[0][1], houses[0][2]

for i in range(1, N):
    # 0 -> 1/2, 1 -> 0/2, 2 -> 0/1
    dp[i][0] = min(dp[i-1][1] + houses[i][0], dp[i-1][2] + houses[i][0])
    dp[i][1] = min(dp[i-1][0] + houses[i][1], dp[i-1][2] + houses[i][1])
    dp[i][2] = min(dp[i-1][0] + houses[i][2], dp[i-1][1] + houses[i][2])

print(min(dp[-1]))