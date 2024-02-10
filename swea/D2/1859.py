# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
#input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    goods = 0
    profit = 0
    for i in range(1, N+1):
        if i == N:
            profit += prices[-1] * goods
            break
        else:
            # 현재 가격과 이전 가격이 같거나 클 때
            if prices[i-1] <= prices[i]:
                profit -= prices[i-1]
                goods += 1
            else:
                # 현재 가격이 이전 가격보다 작을 때: 구매한 물건 개수만큼 이전 가격에 판매
                # 계속 같은 가격이다가 내림차순을 만날 경우 구매하면 안됨
                if goods != 0 and abs(profit // goods) != prices[i-1]:
                    profit += prices[i-1] * goods
                goods = 0
    
    print(f'#{t} {profit}')
