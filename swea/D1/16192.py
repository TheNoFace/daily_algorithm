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

    def move_bus(move, batt=None):
        status['pos_now'] += move
        if not batt:
            if status['batt'] > 0:
                status['batt'] -= move
                return True
            else:
                return False
        else:
            status['batt'] = max_move

    def charge_bus():
        status['batt'] = max_move
        status['pos_past'] = status['pos_now']
        status['charge_count'] += 1

    # 충전소 위치 배열 생성
    charger_loc = [0] * stop
    for i in stop_charger:
        charger_loc[i] = 1

    status = {
        'pos_now': 0,
        'pos_past': 0,
        'batt': max_move,
        'charge_count': 0
    }

    invalid_path = False
    while status['pos_now'] < stop:
        if invalid_path == True:
            status['charge_count'] = 0
            break

        if move_bus(max_move):
            if status['pos_now'] >= stop:
                # print(f'bus has reached destination')
                break

            # print(f'bus moved | {status}')
            if charger_loc[status['pos_now']] == 1:
                # print(f'bus charged @{status["pos_now"]} | {status}')
                charge_bus()
            else:
                # print(f'{status["pos_now"]} doesnt have charger | {status}')
                for i in range(status['pos_now']-1, -1, -1):
                    # print(f'bus returning to {i}')
                    status["pos_now"] = i
                    if charger_loc[i] == 1 and status['pos_now'] > status['pos_past']:
                        # print(f'found charager @{status["pos_now"]}')
                        charge_bus()
                        break
                    elif status['pos_now'] == status['pos_past']:
                        invalid_path = True
                        # print('INVALID PATH PLANNING')
                        break
        else:
            break

    print(f'#{t} {status["charge_count"]}')
