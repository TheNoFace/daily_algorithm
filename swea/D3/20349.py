# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AY3jpQ8qXZ8DFARM

import sys
import os
from collections import deque

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    N, tries = map(int, input().split())
    cards = [i for i in range(1, N + 1)]

    def overhand(cards):
        K = int(N * 0.37)
        temp = []

        for i in range(K):
            temp.append(cards[i + (N - K)])

        for i in range(N - K):
            temp.append(cards[i])

        return temp

    def perfect(cards):
        K = int(N * 0.5)
        temp = []

        for i in range(N - K):
            temp.append(cards[i])
            if i + (N - K) < N:
                temp.append(cards[i + (N - K)])
        
        return temp

    for _ in range(tries):
        cards = overhand(cards)
        cards = perfect(cards)
    
    print(f'#{t}', end=' ')
    print(*cards)
