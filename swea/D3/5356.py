# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO

import sys
import os
from pprint import pprint

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    words = [list(map(str, input())) for _ in range(5)]
    # pprint(words)

    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)

    string = ''
    for c in range(max_length):
        for r in range(5):
            try:
                string += words[r][c]
            except:
                continue
    
    print(f'#{t} {string}')
