# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYQBq9qMREDFAVw&probBoxId=AY1X4zx6gsoDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = input().rstrip()

    # 0~9까지라고 숫자가 나와있으므로,
    # 따로 입력값의 최대값을 구할 이유 X
    count = [0] * 10
    for num in nums:
        count[int(num)] += 1

    max_c = 0
    max_n = 0
    for i in range(10):
        if count[i] >= max_c:
            max_c = count[i]
            max_n = i

    print(f'#{t} {max_n} {max_c}')
