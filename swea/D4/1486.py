# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def dfs(count, picks, height_sum):
    global diff
    if height_sum >= B:
        temp_diff = height_sum - B
        if diff > temp_diff:
            diff = temp_diff
        return

    if count == N:
        return

    # for i in range(N):
    #     if i not in set(picks):
    #         dfs(count, picks + [i], height_sum + heights[i])
    # 재귀 진입
    # 선택
    dfs(count + 1, picks + [count], height_sum + heights[count])
    # 미선택
    dfs(count + 1, picks, height_sum)


T = int(input())
for t in range(1, T + 1):
    # 점원 수 N, 탑 최소 높이 B
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    diff = B
    dfs(0, [], 0)
    print(f"#{t}", diff)
