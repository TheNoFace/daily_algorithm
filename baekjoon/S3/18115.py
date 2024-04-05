# https://www.acmicpc.net/problem/18115

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
options = list(map(int, input().split()))
cards = [i for i in range(1, N + 1)]
origin = deque()

# 1. 제일 위의 카드 1장을 바닥에 내려놓는다.
# 2. 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
# 3. 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.


def shuffle(option, card, origin):

    # 1. 맨 앞 삽입
    if option == 1:
        origin.insert(0, card)
        return

    # 2. 두 번째 삽입
    elif option == 2:
        origin.insert(1, card)
        return

    # 3. 맨 뒤 삽입
    elif option == 3:
        origin.append(card)
        return


for i in range(1, N + 1):
    option = options[i * (-1)]
    card = cards[i - 1]
    shuffle(option, card, origin)

print(*origin, end=" ")
print()
