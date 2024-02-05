# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(1, 1+T):
    N = int(input())
    buses = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stops = [int(input()) for _ in range(P)]

    """
    카운팅 정렬 활용
    - 정류장 최고 번호 (max(stops)) 만큼의 배열 생성: array
    - 혹은 버스 노선 정류장의 최고 번호를 사용
    - buses의 정수를 array의 인덱스로 사용
    """
    # # 최고값 비교
    # stop_nums = []
    # for bus in buses:
    #     stop_nums.append(bus[1])

    # array = [0] * (max(max(stops), max(stop_nums)) + 1)
    array = [0] * 5001
    for bus in buses:
        A, B = bus
        for idx in range(A, B+1):
            array[idx] += 1

    print(f'#{t}', end=' ')
    for stop in stops:
        print(array[stop], end=' ')
    print()