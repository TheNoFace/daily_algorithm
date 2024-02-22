# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWS2dSgKA8MDFAVT

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    audiances = input()

    clappers = 0
    hire = 0
    for idx, i in enumerate(audiances):
        deficit = 0
        if clappers < idx:
            deficit = idx - clappers
        clappers += int(i) + deficit
        hire += deficit

    print(f'#{t} {hire}')
