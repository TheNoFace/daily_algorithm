# https://www.acmicpc.net/problem/24416

## Referenced
# https://www.acmicpc.net/board/view/123191

import sys

input = sys.stdin.readline


# 재귀 함수로 구현된 피보나치 수열의 결과값은 1의 총 합이므로
# 결국 재귀 함수의 계산 회수는 피보나치 수열의 결과값과 동일

# def recursive(n):
#     global count

#     if n == 1 or n == 2:
#         return 1
#     else:
#         count += 1

#     return recursive(n - 1) + recursive(n - 2)


def dynamic(n):
    lst = [0] * n
    lst[0], lst[1] = 1, 1
    count = 0

    for idx, i in enumerate(range(2, n)):
        lst[i] = lst[i - 1] + lst[i - 2]
        count = idx + 1

    return lst[n - 1], count


n = int(input())

# count = 1
# recursive(n)

recursive_count, dynamic_count = dynamic(n)

print(recursive_count, dynamic_count)
