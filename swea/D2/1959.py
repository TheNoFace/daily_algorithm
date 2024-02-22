# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))

    if len(arr_a) > len(arr_b):
        short_arr, long_arr = arr_b, arr_a
    else:
        short_arr, long_arr = arr_a, arr_b
        
    max_value = 0
    for i in range(len(long_arr) - len(short_arr) + 1):
        result = 0
        for j in range(len(short_arr)):
            result += short_arr[j] * long_arr[i+j]
        if result > max_value:
            max_value = result

    print(f'#{t} {max_value}')