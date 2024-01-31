# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYQCjXKMeYDFAVw&probBoxId=AY1X4zx6gsoDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    max_move, stop, charger_count = map(int, input().split())
    stop_charger = list(map(int, input().split()))
    
    pos_now = 0
    pos_past = 0
    charge_count = 0
    invalid_path = False

    charger_loc = [0] * (stop + 1)
    for i in stop_charger:
        charger_loc[i] = 1

    while invalid_path != True:
        pos_now += max_move
        
        if pos_now >= stop:
            break

        if charger_loc[pos_now] == 1:
            pos_past = pos_now
            charge_count += 1
        else:
            for i in range(max_move):
                pos_now -= 1
                if pos_now == pos_past:
                    invalid_path = True
                    charge_count = 0
                    break
                elif charger_loc[pos_now] == 1:
                    pos_past = pos_now
                    charge_count += 1
                    break
    
    print(f'#{t} {charge_count}')