# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

for t in range(1, 11):
    M = int(input())
    chars = [input().rstrip() for _ in range(8)]

    def find_palindrome(chars, M):
        count = 0
        for r in range(8):
            for c in range(8-M+1):
                palindrome = ''
                for i in range(M):
                    if chars[r][c+i] == chars[r][c+M-1-i]:
                        palindrome + chars[r][c+i]
                    else:
                        break
                else:
                    count += 1

        for c in range(8):
            for r in range(8-M+1):
                palindrome = ''
                for i in range(M):
                    if chars[r+i][c] == chars[r+M-1-i][c]:
                        palindrome + chars[r+i][c]
                    else:
                        break
                else:
                    count += 1
        return count

    print(f'#{t} {find_palindrome(chars, M)}')