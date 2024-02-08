# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZOV_w6TKsDFAVw&probBoxId=AY2GP4uqGrgDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
#input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    # V개 노드, E개 간선
    V, E = map(int, input().split())
    # print(f'#{t} V: {V}, E: {E}')
    # 인접 리스트 이용
    adj_list = [[] for _ in range(V+1)]

    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        # 방향 있는 간선이므로 반대 노드는 필요 없음
    
    s_node, t_node = map(int, input().split())
    # print(f'#{t} s_node: {s_node}, t_node: {t_node}')

    # 방문 확인 배열 생성 및 필요 변수 초기화
    visited = [0] * (V+1)
    stack = []
    start = s_node
    visited[start] = 1
    # print(start)

    while visited[t_node] != 1:
        for i in adj_list[start]:
            if visited[i] == 0:
                stack.append(start)
                visited[i] = 1
                start = i
                # print(start)
                break
        # start 노드에 방문 안한 노드가 없을 경우
        else:
            # 스택이 남아있으면 pop해서 start로 초기화
            if stack:
                start = stack.pop()
            # 스택이 비어있으면 탐색 종료
            else:
                break

    if visited[s_node] == 1 and visited[t_node] == 1:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

