# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    array = list(map(int, input().split()))
    
    def count_sort(input_array):
        # 최고 정수 100, 101개인 배열 생성
        count = [0] * 101
        for i in input_array:
            count[i] += 1

        for i in range(1, 101):
            count[i] += count[i-1]
            
        result = [0] * 101
        for i in range(99, -1, -1):
            count[input_array[i]] -= 1
            result[count[input_array[i]]] = input_array[i]

        # n >= 1 이므로 0은 삭제
        result.pop()
        return result

    array = count_sort(array)
    for i in range(N):
        array[-1] -= 1
        array[0] += 1
        array = count_sort(array)

    print(f'#{t} {array[-1] - array[0]}')