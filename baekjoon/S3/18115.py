# https://www.acmicpc.net/problem/18115

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
options = list(map(int, input().split()))
cards = [i for i in range(1, N + 1)]
origin = [0] * N

# 1. 제일 위의 카드 1장을 바닥에 내려놓는다.
# 2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
# 3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.


def shuffle(option, card):

    # 1. 맨 앞 삽입
    if option == 1:
        temp_origin = [0] * N
        # for i in range(N - 1):
        #     temp_origin[i + 1] = origin[i]
        temp_origin[0] = 1
        origin[0] = card
        origin[1:] = temp_origin[1:]
    # 2. 두 번째 삽입
    elif option == 2:
        temp_origin = [0] * N
        for i in range(1, N - 1):
            temp_origin[i + 1] = origin[i]
        origin[1] = card
        origin[2:] = temp_origin[2:]
    # 3. 맨 뒤 삽입
    elif option == 3:
        for idx, i in enumerate(origin):
            if i == 0:
                origin[idx] = card
                break


for i in range(1, N + 1):
    option = options[i * (-1)]
    card = cards[i - 1]
    shuffle(option, card)

print(*origin, end=" ")
print()
