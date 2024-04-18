# https://www.acmicpc.net/problem/1436

import sys

input = sys.stdin.readline

N = int(input())
S = 666
count = 1

while count < N:
    S += 1

    count_six = 0
    in_a_row = False

    for idx, n in enumerate(str(S)):
        # 현재 숫자가 6이라면
        if n == "6":
            # 6이 처음 나왔거나 이전 인덱스가 6이었다면
            if not in_a_row or in_a_row + 1 == idx:
                # 6의 개수와 현재 인덱스 업데이트
                count_six += 1
                in_a_row = idx
        # 현재 숫자가 6이 아니면
        else:
            # 초기화
            count_six = 0
            in_a_row = False

        if count_six >= 3:
            count += 1
            break

print(S)
