# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZSmKPaa1oDFAVw&probBoxId=AY2geIZ6R-gDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

def postfix_result(fx):
    stack = []

    for i in fx:
        # 피연산자라면 스택에 저장
        if i not in '()+-/*':
            if i == '.':
                if len(stack) == 1:
                    return result
                else:
                    return 'error'
            stack.append(int(i))
        # 연산자라면 스택에서 피연산자 2개 추출
        else:
            if len(stack) >= 2:
                right = stack.pop()
                left = stack.pop()
            else:
                return 'error'

            if i == '+':
                result = left + right
            elif i == '-':
                result = left - right
            elif i == '*':
                result = left * right
            elif i == '/':
                result = left // right
            
            stack.append(result)


T = int(input())
for t in range(1, T+1):
    fx = list(input().split())
    print(f'#{t} {postfix_result(fx)}')
