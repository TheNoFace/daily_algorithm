# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def planner(v, total):
    global price

    if total >= price:
        return

    if v >= 12:
        price = min(price, total)
        return

    while True:
        if plans[v] == 0:
            v += 1
            if v == 12:
                price = min(price, total)
                return
        else:
            break

    # 해당 월 v 이용 계획
    # 1. 일일 이용권
    planner(v + 1, total + plans[v] * prices[0])

    # 2. 한달 이용권
    planner(v + 1, total + prices[1])

    # 3. 세달 이용권
    planner(v + 3, total + prices[2])


T = int(input())
for t in range(1, T + 1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    price = prices[-1]

    planner(0, 0)
    print(f"#{t}", price)
