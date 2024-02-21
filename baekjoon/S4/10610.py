# https://www.acmicpc.net/status?problem_id=10610&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

T = 4
for t in range(1, T+1):
    # 완전 탐색: 순열 만들어 30으로 나눠져 떨어지는 가장 큰 수 구하기 -> recursion error
    # 그리디: N을 내림차순 정렬 후, 30으로 나뉘어지면 N 반환, 아니면 -1 반환
    N = int(''.join(sorted(list(map(str, input().rstrip())), reverse=True)))
    print(N) if N % 30 == 0 else print(-1)
