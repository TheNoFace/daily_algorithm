# https://www.acmicpc.net/problem/2839

import sys

input = sys.stdin.readline
sys.setrecursionlimit(5000)

N = int(input())

visited = [0] * (N + 5)
result = -1
has_found = False


def sugar(count, weight_sum):
    global result
    global has_found

    if visited[weight_sum]:
        return
    else:
        visited[weight_sum] = 1

    if weight_sum == N:
        result = count
        has_found = True
        return

    if weight_sum > N:
        return

    if not has_found:
        sugar(count + 1, weight_sum + 5)
    if not has_found:
        sugar(count + 1, weight_sum + 3)


sugar(0, 0)
print(result)
