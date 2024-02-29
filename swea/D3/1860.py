# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    lead = sorted(list(map(int, input().split())))
    
    result = 'Possible'
    breads = 0

    if lead[0] == 0:
        result = 'Impossible'
    else:
        i = 1
        while i <= lead[-1]:
            if i % M == 0:
                breads += K

            if i in lead:
                if breads != 0:
                    breads -= 1
                else:
                    result = 'Impossible'
                    break
            
            i += 1

    print(f'#{t} {result}')
