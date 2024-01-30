# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYQBq9qMREDFAVw&probBoxId=AY1X4zx6gsoDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    array = list(map(int, input().rstrip()))

    K = 0
    for i in array:
        if i > K:
            K = i
    
    """
    N: 자리수
    K: 가장 큰 수
    count: 원소 수(길이)가 K+1개인 배열
    temp: 정렬된 array를 반환할 배열 (길이 N)
    """
    count = [0] * (K + 1)

    for i in array:
        count[i] += 1

    max_c = 0
    max_n = 0
    for i in range(0, K+1):
        if count[i] >= max_c:
            max_c = count[i]
            max_n = i

    print(f'#{t} {max_n} {max_c}')
