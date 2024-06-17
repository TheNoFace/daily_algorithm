# https://www.acmicpc.net/problem/10844

## Referenced
# https://www.acmicpc.net/board/view/122963

import sys

input = sys.stdin.readline

N = int(input())
count = 0

# 끝 자리가 0~9로 끝나는 계단 수의 개수를 저장할 배열
# 각 행의 열은 끝자리 숫자를 의미
dp = [[0] * 10 for _ in range(N + 1)]

# 길이가 1인 계단 수의 개수 초기화
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        # 끝 자리가 0 인 계단 수의 개수는 (N - 1) 길이의 계단 수 중 끝 자리가 1인 계단 수의 개수
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        # 끝 자리가 9 인 계단 수의 개수는 (N - 1) 길이의 계단 수 중 끝 자리가 8인 계단 수의 개수
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        # 끝 자리가 0, 9가 아닌 계단수의 개수는 (N - 1) 길이의 계단 수 중 끝 자리가 j - 1 혹은 j + 1인 계단 수의 개수
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)
