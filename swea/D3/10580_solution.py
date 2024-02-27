# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXO8QBw6Qu4DFAXS

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    def get_result():
        count = 0
        # i: 다른 선과 비교할 현재 선
        # target: i선과 비교 대상인 선
        for i in range(len(arr)):
            for target in range(i):
                i_a, i_b = (arr[i][0], arr[i][1])
                # tar_a: target 선에 연결된 가장 큰 수
                tar_a, tar_b = (arr[target][0], arr[target][1])
                if i_b < tar_b:
                    count += 1
        return count

    N = int(input())
    arr = []

    for n in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))

    # 각 원소의 첫 번째 원소(시작점)를 기준으로 오름차순 정렬
    arr.sort(key=lambda x: x[0])
    result = get_result()

    print(f'#{t} {result}')