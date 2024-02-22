# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]
    hotel = [0] * 401
    count = 1  # 모든 경로가 겹치지 않으면 최소 단위 시간은 1

    for idx, student in enumerate(students):
        hotel[student[0]] = hotel[student[1]] = idx + 1

    stack = []
    # for i in hotel:
    #     if i != 0:
    #         if not stack:
    #             stack.append(i)
    #         else:
    #             if stack[-1] != i and i not in stack:
    #                 stack.append(i)
    #                 count += 1
    #             elif stack[-1] == i:
    #                 stack.pop()

    sorted_hotel = []
    for i in hotel:
        if i != 0:
            sorted_hotel.append(i)

    single_time = False
    for i in range(N * 2 - 1):
        if not stack:
            stack.append(sorted_hotel[i])
        else:
            # TODO: 스택 top가 홀, 다음이 짝이면 +1?
            if (
                stack[-1] != sorted_hotel[i]
                and sorted_hotel[i] not in stack
                and not single_time
            ):
                stack.append(sorted_hotel[i])
                count += 1
                if sorted_hotel[i] == sorted_hotel[i+1]:
                    single_time = True
            elif stack[-1] == sorted_hotel[i]:
                stack.pop()

    print(f"#{t} {count}")
