# https://www.acmicpc.net/status?problem_id=10610&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

T = 4
for t in range(1, T+1):
    N = list(map(str, input().rstrip()))
    
    # 완전 탐색: 순열 만들어 30으로 나눠져 떨어지는 가장 큰 수 구하기
    # 그리디: 가장 큰 숫자를 만들어보고, 나누어 떨어지지 않으면 순열 만들기?
    def perm_maker(i, k, arr):
        if i == k:
            num = int(''.join(arr))
            result = max_dividable(num)
            if result != -1:
                return result
        else:
            for j in range(i, k):
                arr[i], arr[j] = arr[j], arr[i]
                perm_maker(i+1, k, arr)
                arr[j], arr[i] = arr[i], arr[j]
        return -1

    def max_dividable(n):
        if n % 30 == 0: return n
        else: return -1

    max_N = int(''.join(sorted(N, reverse=True)))
    if max_dividable(max_N) == max_N:
        print(max_N)
    else:
        print(perm_maker(0, len(N), N))