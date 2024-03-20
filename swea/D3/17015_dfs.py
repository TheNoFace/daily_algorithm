# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYdFX2OqvfMDFAVa&probBoxId=AY5ZiI-qG38DFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def dfs(v):
    stack = [v]
    visited[v] = 1

    while True:
        for adj in adjl[v]:
            if not visited[adj]:
                stack.append(v)
                visited[adj] = 1
                v = adj
                break
        else:
            if stack:
                v = stack.pop()
            else:
                return


def dfs_recursive(v):
    visited[v] = 1

    for adj in adjl[v]:
        if not visited[adj]:
            dfs_recursive(adj)


T = int(input())
for t in range(1, T + 1):
    # 서로소 집합 개수 출력
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    visited = [0] * N
    adjl = [[] for _ in range(N)]
    for i in range(0, len(arr), 2):
        a, b = arr[i] - 1, arr[i + 1] - 1
        adjl[a].append(b)
        adjl[b].append(a)

    count = 0
    for i in range(N):
        if not visited[i]:
            # dfs(i)
            dfs_recursive(i)
            count += 1

    print(f"#{t}", count)
