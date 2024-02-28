# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcliIFqNg8DFAVa&probBoxId=AY3tOLq6DUIDFAUZ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    cards = list(map(int, input().split()))
    winner = 0
    p1, p2 = [], []

    def be_greedy(lst):
        """
            run    : 1 반환
            triplet: 2 반환
        """
        # index 오류 방지용 더미 인덱스 +2
        count = [0] * 12
        for i in lst:
            count[i] += 1

        index = 0
        while index < 10:
            if count[index] >= 3:
                return 1
            elif count[index] >= 1 and count[index+1] >= 1 and count[index+2] >= 1:
                return 2
            index += 1
        return 0


    for i in range(6):
        if i < 2:
            p1.append(cards[i*2])
            p2.append(cards[i*2+1])
        else:
            p1.append(cards[i*2])
            if be_greedy(p1) != 0:
                winner = 1
                break
            p2.append(cards[i*2+1])
            if be_greedy(p2) != 0:
                winner = 2
                break

    print(f'#{t} {winner}')
