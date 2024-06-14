# https://www.acmicpc.net/problem/1932

import sys

input = sys.stdin.readline

n = int(input())

triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[] for _ in range(n)]
dp[0].append(triangle[0][0])

for i in range(1, n):
    for j in range(len(dp[i-1])):
        if dp[i]:
            dp[i][-1] = max(dp[i][-1], dp[i-1][j] + triangle[i][j])
        else:
            dp[i].append(dp[i-1][j] + triangle[i][j])
        dp[i].append(dp[i-1][j] + triangle[i][j+1])

print(max(dp[-1]))