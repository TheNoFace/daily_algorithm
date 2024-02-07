# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZJQ6Q6RKADFAVw&probBoxId=AY2BmSDqHpsDFAXh 

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input_16476.txt', 'r')
input = sys.stdin.readline

parenthesis = ['(', ')', '{', '}']

T = int(input())
for t in range(1, T+1):
    test = input().rstrip()

    stack = []
    # 문자열 검사
    for string in test:
        # 괄호 유무 검사
        if string in parenthesis:
            # 괄호라면, 스택이 비어있지 않고 닫는 괄호인지 검사
            if stack and (string == ')' or string == '}'):
                # 괄호 종류 검사
                if stack[-1] == '{' and string == '}':
                    stack.pop()
                elif stack[-1] == '(' and string == ')':
                    stack.pop()
            # 빈 스택이거나 여는 괄호라면 스택에 추가
            elif not stack or (string == '(' or string == '{'):
                    stack.append(string)
            else:  # wtf?
                print(f'#{t} 0')
                break
    # 문자열 검사 종료 후 스택 확인
    else:
        # 비어있지 않으면 잘못된 괄호
        if not stack:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')