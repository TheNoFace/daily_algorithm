# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZJRQT6RQ0DFAVw&probBoxId=AY2BmSDqHpsDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
#input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    test = input()
    
    stack = []
    for string in test:
        if stack and stack[-1] == string:
            stack.pop()
        else:
            stack.append(string)
    print(f'#{t} {len(stack)}')