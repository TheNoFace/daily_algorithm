# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

for t in range(1, 11):
    t, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    adj_list = [[] for _ in range(100)]

    for i in range(N):
        n1, n2 = nodes[i*2], nodes[i*2+1]
        adj_list[n1].append(n2)

    visited = [0] * 100
    visited[0] = 1
    stack = []
    start = 0

    # B 위치에 도달할 때까지
    while visited[99] != 1:
        # 현재 시작지점의 인접 정점 중
        for adj in adj_list[start]:
            # 방문한 적이 없는 정점이라면
            if visited[adj] == 0:
                # 이전 시작 위치를 스택에 push
                stack.append(start)
                # 현재 정점 방문 표시
                visited[adj] = 1
                # 현재 정점을 시작점으로 재설정
                start = adj
                break
        else:
            # 스택이 비어있지 않으면
            if stack:
                # 직전 갈림길로 시작 위치 초기화
                start = stack.pop()
            # 스택이 비어있으면
            else:
                break

    if visited[99] == 1:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')