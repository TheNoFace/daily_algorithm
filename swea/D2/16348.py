# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYvXypKDrkDFAVw&probBoxId=AY1768RaC0oDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    text = [input().rstrip() for _ in range(N)]

    def check_circular(text, N, M):
        '''
            2차원 배열을 순회하면서 현재 인덱스에서 M만큼 떨어진 글자가 현재 위치의 글자가 같은지 확인
            M칸 떨어진 글자 회문 검사: 현재 인덱스(c) + 회문 길이(M) - 1 - 비교 횟수(i)
        '''

        # 행 우선 검사
        for r in range(N):
            for c in range(N-M+1):
                reversed_char = ''
                for i in range(M):
                    if text[r][c+i] == text[r][c+M-1-i]:
                        reversed_char += text[r][c+i]
                    else:
                        break
                else:
                    return reversed_char

        # 열 우선 검사
        for c in range(N):
            for r in range(N-M+1):
                reversed_char = ''
                for i in range(M):
                    if text[r+i][c] == text[r+M-1-i][c]:
                        reversed_char += text[r+i][c]
                    else:
                        break
                else:
                    return reversed_char

    print(f'#{t} {check_circular(text, N, M)}')