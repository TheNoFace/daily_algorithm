# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYvXfaaDp0DFAVw&probBoxId=AY14AqXqTP4DFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    strings = [list(map(str, ''.join(input()))) for _ in range(2)]

    # 뒷 리스트를 앞 리스트 길이만큼 순회하면서 동일한 문자열이면 반환
    for i in range(len(strings[1]) - len(strings[0]) + 1):
        if strings[0] == strings[1][i:i+len(strings[0])]:
            result = 1
            break
        else:
            result = 0
    print(f'#{t} {result}')