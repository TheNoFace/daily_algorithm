# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    deck = list(map(str, input().split()))

    a = 0
    b = N // 2 if N % 2 == 0 else N // 2 + 1

    print(f'#{t}', end=' ')

    # # 투포인트 알고리즘
    # for i in range(N//2):
    #     print(deck[a], deck[b], end=' ')
    #     a += 1
    #     b += 1

    # if N % 2 != 0:
    #     print(deck[a], end=' ')
    # print()

    if N % 2 == 0:
        for i in range(N//2):
            print(deck[i], deck[i+N//2], end=' ')
    else:
        for i in range(N//2):
            print(deck[i], deck[i+N//2+1], end=' ')
        print(deck[N//2], end=' ')
    print()