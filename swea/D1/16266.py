# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYk_zdayGUDFAVw&probBoxId=AY1d6dFajWsDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())
set_a = [n for n in range(1, 13)]

for t in range(1, T+1):
    # 부분 집합 크기가 N, 부분 집합 원소의 합이 K인 부분 집합의 개수
    N, K = map(int, input().split())
    subset_count = 0

    def counter(input, value):
        count = 0
        for i in f'{input:b}':
            if i == str(value):
                count += 1
        return count

    # 원소가 12개인 집합의 부분집합 생성
    for i in range(1, 1 << 12):  # 공집합 제외
        # 원소의 개수가 N개라면
        if counter(i, 1) == N:
            subset_sum = 0
            for j in range(12):
                if i & (1 << j):
                    subset_sum += set_a[j]
                    if subset_sum > K:
                        break
                    
            if subset_sum == K:
                subset_count += 1
        
    print(f'#{t} {subset_count}')