# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PyTLqAf4DFAUq

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    word = input()
    for i in range(len(word)):
        if word[i] == word[-(i+1)]:
            pass
        else:
            print(f'#{t} 0')
            break
    else:
        print(f'#{t} 1')
