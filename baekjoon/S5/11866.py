# https://www.acmicpc.net/problem/11866

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(N)]

print("<", end="")

result = []
total, idx = 0, 0
while total < N:
    count = 0
    while count < K:
        if arr[idx] != -1:
            count += 1
            if count == K:
                break
        idx = idx + 1 if idx < N - 1 else 0
    # print(arr[idx] + 1, ', ')
    result.append(str(arr[idx] + 1))
    arr[idx] = -1
    total += 1

print(", ".join(result), end="")
print(">", end="")
print()
