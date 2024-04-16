# https://www.acmicpc.net/problem/1620

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

monster_list = [0] * (N + 1)
monster_dict = {}

for i in range(1, N + 1):
    monster = input().rstrip()
    monster_dict[monster] = i
    monster_list[i] = monster

for _ in range(M):
    query = input().rstrip()
    try:
        idx = int(query)
        print(monster_list[idx])
    except:
        print(monster_dict[query])
