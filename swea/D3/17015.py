# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYdFX2OqvfMDFAVa&probBoxId=AY5ZiI-qG38DFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def find_set_compression(x):
    if parents[x] != x:
        parents[x] = find_set_compression(parents[x])
    return parents[x]


def union(a, b):
    a = find_set_compression(a)
    b = find_set_compression(b)

    if a == b:
        return

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


T = int(input())
for t in range(1, T + 1):
    # 서로소 집합 개수 출력
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # make-set
    parents = [i for i in range(N)]

    for i in range(0, len(arr), 2):
        a, b = arr[i] - 1, arr[i + 1] - 1
        union(a, b)

    # 최종 서로소 집합 개수를 구하려면, 개수 도출 전 각 노드의 부모를
    # 최상위 대표자로 설정하는 경로 압축 과정이 필요함
    for i in range(N):
        find_set_compression(i)

    print(f"#{t}", len(set(parents)))
