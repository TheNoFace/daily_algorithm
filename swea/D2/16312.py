# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYqKXCKE6gDFAVw&probBoxId=AY1iV5DKi8IDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())

    def binary_search(page, a_page, b_page):
        a_start = b_start = 1
        a_end = b_end = page
        a_fin = b_fin = False

        while True:
            if a_fin and not b_fin:
                return 'A'
            elif not a_fin and b_fin:
                return 'B'
            elif a_fin and b_fin:
                return '0'
            else:
                a_center = (a_start + a_end) // 2
                if a_page < a_center:
                    a_end = a_center
                elif a_page > a_center:
                    a_start = a_center
                else:
                    a_fin = True
                
                b_center = (b_start + b_end) // 2
                if b_page < b_center:
                    b_end = b_center
                elif b_page > b_center:
                    b_start = b_center
                else:
                    b_fin = True

    print(f'#{t} {binary_search(P, A, B)}')