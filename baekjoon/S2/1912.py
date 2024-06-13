# https://www.acmicpc.net/problem/1912

## Referenced
# https://lemon27.tistory.com/10

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# n개 원소까지의 합을 저장할 배열
dp = [0] * n
# 최소 1개의 원소를 선택
dp[0] = arr[0]

for i in range(1, n):
    # (직전 원소까지의 합 + 현재 원소) 보다 현재 원소가 더 크다면
    # 현재 원소부터의 합을 구하는 것
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))
