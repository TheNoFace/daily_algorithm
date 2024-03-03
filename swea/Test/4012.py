# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

import sys
import os
from pprint import pprint
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline


T = int(input())
for t in range(1, T+1):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    diff = 20000 * (N // 2)
    ingredients = [n for n in range(N)]

    """
        N개 재료를 N//2개씩 나눠서 각각 요리
        A 요리에 사용할 재료가 결졍되면 B 요리 재료는 자동으로 결정
        각 조합별 시너지 계산 후 반환
    """
    def picker(index, count, picked, used):
        global diff

        # 종료 조건:
        # 1) 첫 재료가 0이 아닐 경우
        # 첫 재료로 0이 포함된 순열이 모두 생성되면 A, B로 나뉠 수 있는 모든 조합 완성
        if picked and picked[0] != 0:
            return
        # 2) N//2개 선택 완료
        elif count == N // 2:
            pick_list = []
            pick_list.append(picked)
            food_b = []
            for i in ingredients:
                if i not in picked:
                    food_b.append(i)
            pick_list.append(food_b)

            # 조합별 시너지 차이 계산
            temp_diff = 0
            for idx, food in enumerate(pick_list):
                for i in range(N // 2 - 1):
                    for j in range(i + 1, N // 2):
                        synergy = foods[food[i]][food[j]] + foods[food[j]][food[i]]
                        temp_diff = temp_diff + synergy if idx == 0 else temp_diff - synergy

            if diff > abs(temp_diff):
                diff = abs(temp_diff)
            return
        else:
            # 중복 없는 순열 생성
            for pick in ingredients[index:]:
                if pick not in used:
                    picker(index, count + 1, picked + [pick], used + [pick])
                picker(index + 1, count, picked, used)
                return

    picker(0, 0, [], [])
    print(f'#{t} {diff}')
