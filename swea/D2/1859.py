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
    
    profit = 0
    max_price = prices.pop(-1)
    while prices:
        price = prices.pop(-1)
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price

    print(f'#{t} {profit}')
