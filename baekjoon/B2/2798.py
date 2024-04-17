# https://www.acmicpc.net/problem/2798

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
diff = M


def selector(idx, pick, pick_sum):
    global diff

    if len(pick) == 3:
        if pick_sum > M:
            return

        if diff > M - pick_sum:
            diff = M - pick_sum
        return

    if idx == N:
        return

    selector(idx + 1, pick + [cards[idx]], pick_sum + cards[idx])
    selector(idx + 1, pick, pick_sum)


selector(0, [], 0)
print(M - diff)
