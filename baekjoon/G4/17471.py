# https://www.acmicpc.net/problem/17471

## Referenced
# https://cotak.tistory.com/66

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
adjl = [[] for _ in range(N + 1)]
not_connected = True
diff = sum(people)

for i in range(1, N + 1):
    adjs = list(map(int, input().split()))
    for j in range(adjs[0]):
        adjl[i].append(adjs[j + 1])


# 개수가 N // 2개인 부분 집합 도출
def subset(idx, picks):
    global diff
    global not_connected

    if len(picks) == N // 2 or idx == N + 1:
        if not picks:
            return

        # BFS로 picks와 not picks의 연결 확인
        not_picks = [i for i in range(1, N + 1) if i not in picks]
        nodes_a, sum_a = bfs(picks)
        nodes_b, sum_b = bfs(not_picks)

        if nodes_a + nodes_b == N:
            not_connected = False
            diff = min(diff, abs(sum_a - sum_b))
        return

    subset(idx + 1, picks + [idx])
    subset(idx + 1, picks)


def bfs(picks):
    v = picks[0]
    q = deque()
    q.append(v)
    visited = [0] * (N + 1)
    visited[v] = 1
    nodes = 1
    sums = people[v - 1]

    while q:
        v = q.popleft()
        for adj in adjl[v]:
            if not visited[adj] and adj in picks:
                visited[adj] = 1
                q.append(adj)
                nodes += 1
                sums += people[adj - 1]
    return nodes, sums


subset(1, [])
if not_connected:
    print(-1)
else:
    print(diff)
