# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

# brute-force search
def brute_force(pattern, text):
    p_length = len(pattern)
    t_length = len(text)
    p_index = 0  # 패턴 인덱스 == 패턴 비교 횟수
    t_index = 0
    result = 0

    while t_index <= t_length - p_length + 1:
        # 패턴과 텍스트가 불일치하면
        if text[t_index] != pattern[p_index]:
            # 패턴 비교한 횟수만큼 다시 비교 시작점 이동
            t_index -= p_index
            p_index = -1
        # 패턴과 텍스트가 일치하면 다음 인덱스끼리 비교
        t_index += 1
        p_index += 1
    
        if p_index == p_length:
            result += 1
            p_index = 0

    return result

for t in range(1, 11):
    input()  # 불필요한 입력은 버림
    P = input().rstrip()
    T = input().rstrip()
    
    print(f'#{t} {brute_force(P, T)}')
