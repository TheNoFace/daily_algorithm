# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    is_duplicated = False

    # 행        
    for r in range(9):
        if not is_duplicated:
            compare = []
            for c in range(9):
                if sudoku[r][c] in compare:
                    is_duplicated = True
                    break
                else:
                    compare.append(sudoku[r][c])
        else:
            break

    # 열
    if not is_duplicated:
        for c in range(9):
            if not is_duplicated:
                compare = []
                for r in range(9):
                    if sudoku[r][c] in compare:
                        is_duplicated = True
                        break
                    else:
                        compare.append(sudoku[r][c])
            else:
                break

    # 작은 그리드
    while not is_duplicated:
        for r in range(0, 9, 3):
            c = 0
            while c <= 6:
                compare = []
                for i in range(3):
                    for j in range(3):
                        if sudoku[r+i][c+j] in compare:
                            is_duplicated = True
                            break
                        else:
                            compare.append(sudoku[r][c])
                else:
                    c += 3
        else:
            break

    print(f'#{t} ', end='')
    if is_duplicated:
        print('0')
    else:
        print('1')