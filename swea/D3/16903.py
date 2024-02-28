# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYclhJz6NeUDFAVa&probBoxId=AY3tOLq6DUIDFAUZ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    cargos = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    load = [0] * M
    pick = []
    max_weight = 0

    trucks.sort(reverse=True)
    cargos.sort(reverse=True)
    
    for i in range(len(trucks)):
        for j in range(len(cargos)):
            if cargos[j] <= trucks[i] and j not in pick and load[i] == 0:
                load[i] = cargos[j]
                pick.append(j)
                max_weight += cargos[j]

    print(f'#{t} {max_weight}')
