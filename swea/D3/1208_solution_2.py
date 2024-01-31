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
    
    while N > 0:
        max_index = 0
        min_index = 0
        max_height = 0
        min_height = 100

        for i in range(100):
            if array[i] > max_height:
                max_height = array[i]
                max_index = i
        
            if array[i] < min_height:
                min_height = array[i]
                min_index = i

        array[max_index] -= 1
        array[min_index] += 1
        N -= 1
    
    # last check
    max_height = 0
    min_height = 100

    for i in range(100):
        if array[i] > max_height:
            max_height = array[i]
        if array[i] < min_height:
            min_height = array[i]
    
    print(f'#{t} {max_height - min_height}')
    