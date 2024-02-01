# https://www.acmicpc.net/problem/1065

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

def series_counter(N):
    print(N, end=' ')
    if N < 100:
        return N
    else:
        result = 0
        num_length = 3
        for i in range(111, N+1):
            if i == 1000:
                result -= 1
            num = []
            for _ in range(num_length):
                modulo = i % 10
                num.append(modulo)
                i = i // 10
            # print(*num[::-1], num)

            diff_init = (num[0] - num[1]) 
            if (num[0] - num[1]) == (num[1] - num[2]):
                # print(f'{num} is in series')
                result += 1

        return 99 + result

T = int(input())
for t in range(1, 1+T):
    print(series_counter(int(input())))

