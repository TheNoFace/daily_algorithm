# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYqJ3jqE0EDFAVw&probBoxId=AY1iV5DKi8IDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

input = sys.stdin.readline

def selection_sort(a, N):
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if a[min_index] > a[j]:
                min_index = j
        a[min_index], a[i] = a[i], a[min_index]
    return a

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = selection_sort(arr, N)
    
    # 맨 앞, 맨 뒤 숫자를 하나씩 가져옴
    result = []
    for i in range(5):
        result.append(arr.pop())
        result.append(arr.pop(0))

    print(f'#{t}', *result)
