# https://www.acmicpc.net/status?problem_id=11725&user_id=fprhqkrtk303
# https://www.acmicpc.net/board/view/99171

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())

"""
    자식 노드의 개수가 최대 2개가 아닐 수도 있기 때문에
    이진 트리 형식으로 풀이하면 안됨
    DFS / BFS 로 풀이
"""

adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)


def bfs(graph, v):
    parent = [0] * (N + 1)
    q = deque()
    q.append(v)

    while q:
        t = q.popleft()
        for node in adj_list[t]:
            # 루트 노드 1는 무시
            if node != 1 and parent[node] == 0:
                parent[node] = t
                q.append(node)

    for i in range(2, N + 1):
        print(parent[i])


bfs(adj_list, 1)
