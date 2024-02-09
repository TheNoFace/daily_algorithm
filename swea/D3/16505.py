# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZOVq9KTH8DFAVw&probBoxId=AY2GP4uqGrgDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
#input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    
    # f(n) = f(n-1) + 2 * f(n-2)
    def papers(N):
        n = N // 10
        if n == 1:
            return 1
        if n == 2:
            return 3
        return papers(N-10) + 2 * papers(N-20)

    print(f'#{t} {papers(N)}')
