# https://www.acmicpc.net/problem/31476

## Referenced
# https://www.acmicpc.net/board/view/138256

import sys
from collections import deque

input = sys.stdin.readline


def twintail(v):
    # 양갈래로 갈라질 때만 T 증가
    # 깊이별 최대 T 저장
    visited = [0] * 2**D
    depth = [False] * D
    time = 0

    q = deque()
    # 시작점과 직전까지의 분할 횟수 저장
    q.append((v, 0))
    visited[v] = 1

    while q:
        s, t = q.popleft()
        # 좌우 자식이 둘다 존재한다면 양갈래로 나뉨
        if left[s] and right[s]:
            t += 1
        for node in adjl[s]:
            if not visited[node]:
                q.append((node, t))
                visited[node] = visited[s] + 1
                # 깊이 방문 확인
                if not depth[visited[s] - 1]:
                    depth[visited[s] - 1] = 0
                # 최장 소요시간 등록
                if depth[visited[s] - 1] < t:
                    depth[visited[s] - 1] = t

    for i in depth:
        if i is not False:
            time += U + i * T
    return time


def ponytail(v):
    visited = [0] * 2**D
    time = 0

    stack = []
    stack.append(v)
    visited[v] = 1

    while True:
        for node in adjl[v]:
            if not visited[node]:
                stack.append(v)
                visited[node] = visited[v] + 1
                v = node
                time += U
                break
        else:
            if stack:
                v = stack.pop()
                # 부모 -> 루트노드까지 모든 간선 탐색이 완료됐다면 return
                in_search = False
                count = 0
                while not in_search:
                    for node in adjl[v]:
                        if not visited[node]:
                            in_search = True
                            break
                    else:
                        v = parent[v]
                        count += 1
                        if v == 1:
                            for node in adjl[1]:
                                if not visited[node]:
                                    in_search = True
                                    break
                        else:
                            if v == 0:
                                return time
                time += U * (count + 1)


D, N, U, T = map(int, input().split())

parent = [0] * 2**D
left = [0] * 2**D
right = [0] * 2**D

# 트리 생성
for i in range(1, 2**D):
    parent[i] = i // 2
    if i >= 2:
        # 짝수는 왼쪽 자식
        if i % 2 == 0:
            left[i // 2] = i
        # 홀수는 오른쪽 자식
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

# 부서진 길목 제거
for i in range(N):
    s, e = map(int, input().split())
    adjl[s].remove(e)
    adjl[e].remove(s)

    # 짝수는 왼쪽 자식
    if e % 2 == 0:
        left[s] = 0
    # 홀수는 오른쪽 자식
    else:
        right[s] = 0

time_twintail = twintail(1)
time_ponytail = ponytail(1)

if time_twintail < time_ponytail:
    print(":blob_twintail_aww:")
elif time_twintail > time_ponytail:
    print(":blob_twintail_sad:")
else:
    print(":blob_twintail_thinking:")
