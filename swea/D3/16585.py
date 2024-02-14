# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?contestProbId=AYZXgPFKgIMDFAVw&solveclubId=AYzyVay6v90DFAXz&probBoxId=AY2lPqk6jykDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

s, r, p = 1, 2, 3

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    def tournament(i, j):
        """
           i: 시작 번호
           j: 종료 번호(N)
           최소 단위로 쪼갠 후에 최소 단위에서 승자를 가려냄 
        """
        # 종료 조건: 최소 단위로 쪼개졌을 때
        if i == j:
            # 최소 단위에선 자기 자신이 승자이므로, 자기 자신을 반환
            return i
        else:
            left = tournament(i, (i+j)//2)
            right = tournament((i+j)//2+1, j)
            return rsp(left, right)

    def rsp(l, r):
        left = cards[l-1]
        right = cards[r-1]

        # 비겼을 경우
        if left == right:
            return l
        else:
            if left == 1 and right == 3:    # 가위 > 보
                return l
            elif left == 2 and right == 1:  # 바위 > 가위
                return l
            elif left == 3 and right == 2:  # 보 > 바위
                return l
            else:
                return r

    print(f'#{t} {tournament(1, N)}')
