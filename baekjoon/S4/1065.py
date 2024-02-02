# https://www.acmicpc.net/problem/1065

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

def series_counter(N):
    # print(N, end=' ')
    if N < 100:
        return N
    elif N == 1000:
        return 144
    else:
        result = 0
        num_length = 3
        for i in range(111, N+1):
            num = []
            for _ in range(num_length):
                num.append(i % 10)
                i = i // 10
            # print(*num[::-1], num)

            diff_init = (num[0] - num[1]) 
            if (num[0] - num[1]) == (num[1] - num[2]):
                # print(f'{num} is in series')
                result += 1

        return 99 + result

print(series_counter(int(input())))
