# https://www.acmicpc.net/status?problem_id=5568&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

T = int(input().rstrip())

for t in range(1, T+1):
    N = int(input().rstrip())
    K = int(input().rstrip())
    cards = [input().rstrip() for _ in range(N)]
    picks = []
    
    # N개 카드로 만들 수 있는 수열 만들기
    def perm_swap(i, n):
        """
            i: 시작 위치
            k: 카드 개수
        """
        if i == n:
            print(cards)
            return
        else:
            for j in range(i, n):
                cards[i], cards[j] = cards[j], cards[i]
                perm_swap(i+1, n)
                # 재귀가 끝나면 바꾼 위치 초기화
                cards[j], cards[i] = cards[i], cards[j]

    # perm_swap(0, N)

    def perm_maker(picked, n, result):
        """
            picked: 지금까지 선택한 card
            n: 지금까지 선택한 개수 (n <= k)
            result: 선택한 카드로 만든 정수
        """
        # 종료 조건
        if n == K:
            # 지금까지 고른 카드가 picks에 없다면
            if result not in picks:
                picks.append(result)
            return

        for i in range(len(cards)):
            if i not in picked:
                picked.append(i)
                new_result = result + cards[i]
                perm_maker(picked, n+1, new_result)
                picked.pop()

    perm_maker([], 0, '')
    print(len(picks))
