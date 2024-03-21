# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYdJ95_aDiADFAVa&probBoxId=AY5evUOan8YDFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    # 대표자 찾기
    x = find_set(x)
    y = find_set(y)
    if x != y:
        if x < y:
            parents[y] = x
        else:
            parents[x] = y


T = int(input())
for t in range(1, T + 1):
    # Kruskal Algorithm
    V, E = map(int, input().split())
    edges = []
    count = 0
    weight_sum = 0

    for _ in range(E):
        a, b, w = map(int, input().split())
        edges.append((a, b, w))

    # 간선별 가중치 기준 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # 대표자 생성
    parents = [i for i in range(V + 1)]

    # 가중치 오름차순 간선 탐색
    for edge in edges:
        a, b, w = edge

        # 사이클 발생 유무 판단
        if find_set(a) != find_set(b):
            # 사이클이 발생하지 않으면 연결
            union(a, b)
            print(a, b)
            weight_sum += w
            count += 1

        if count == V:
            break

    print(f'#{t}', weight_sum)