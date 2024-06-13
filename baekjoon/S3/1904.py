# https://www.acmicpc.net/problem/1904

## Referenced
# https://velog.io/@dlwns97/백준-1904번-01타일

import sys

input = sys.stdin.readline


# 재귀 + 메모이제이션?
# tiles = ["1", "00"]
# count = 0
# def func(string):
#     global count
#     if len(string) >= N:
#         if len(string) == N:
#             count += 1
#             print(string)
#         return

#     func(string + "1")
#     func(string + "00")


def func(N):
    """
    f[i] 수열 개수: f[i - 1]에 '1' 붙이기 + f[i - 2]에 '00' 붙이기
    f[i] = f[i - 1] + f[i - 2]
    """

    if N == 1:
        return 1
    elif N == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, N + 1):
            result = (a + b) % 15746
            a = b
            b = result
        return result


N = int(input())
print(func(N))
