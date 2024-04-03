# https://www.acmicpc.net/problem/31476

import sys
from collections import deque

input = sys.stdin.readline

# 양갈래 블롭: BFS
# 포니테일 블롭: DFS
# 시작이 1층, 깊이 D는 기존 깊이 D - 1
# 시작 1층 포함 깊이 3층의 노드 개수는 2^{2+1}-1 = 7개


# 완전 이진 트리의 간선 개수는 노드 개수 - 1
def twintail(v):
    visited = [0] * 2**D
    time = 0

    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        s = q.popleft()
        for node in adjl[s]:
            if not visited[node]:
                q.append(node)
                visited[node] = visited[s] + 1
        if visited[s] < D:
            time += U + visited[s] * T

    return time


def ponytail(v):
    visited = [0] * 2**D
    time = 0

    stack = []
    stack.append(v)
    visited[v] = 1
    # print(v)

    while True:
        for node in adjl[v]:
            if not visited[node]:
                stack.append(v)
                visited[node] = visited[v] + 1
                v = node
                # print(v)
                time += U
                if v == 2**D - 1:
                    return time
                break
        else:
            if stack:
                v = stack.pop()
                # print(v)
                time += U
            else:
                return time


D, N, U, T = map(int, input().split())

parent = [0] * 2**D
left = [0] * 2**D
right = [0] * 2**D

# 트리 생성
for i in range(1, 2**D):
    parent[i] = i // 2
    if i >= 2:
        # 홀수는 왼쪽 자식
        if i % 2 == 0:
            left[i // 2] = i
        # 짝수는 오른쪽 자식
        else:
            right[i // 2] = i

# 인접리스트 생성
adjl = [set() for _ in range(2**D)]
for i in range(1, 2**D):
    if parent[i]:
        adjl[i].add(parent[i])
    if left[i]:
        adjl[i].add(left[i])
    if right[i]:
        adjl[i].add(right[i])

# print(adjl)
for i in range(N):
    s, e = map(int, input().split())
    adjl[s].remove(e)
    adjl[e].remove(s)

# print(adjl)
time_twintail = twintail(1)
time_ponytail = ponytail(1)
# print(time_twintail)
# print(time_ponytail)

if time_twintail > time_ponytail:
    print(":blob_twintail_aww:")
elif time_twintail < time_ponytail:
    print(":blob_twintail_sad:")
else:
    print(":blob_twintail_thinking:")
