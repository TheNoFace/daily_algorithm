import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    
    # 구간합의 최소, 최대값의 차이
    max_sum = 0
    min_sum = 10000 * M

    # 반복을 하면서 구간합 정하기
    # (N - M + 1): 합을 구할 수 있는 인덱스까지만 순회 제한
    for i in range(0, N-M+1):
        sub_sum = 0
        for j in range(0, M):
            sub_sum += array[i+j]

        # 구간합을 다 구한 이후 최대값과 최소값 구하기
        max_sum = sub_sum if sub_sum > max_sum else max_sum
        min_sum = sub_sum if sub_sum < min_sum else min_sum

    print(f'#{t} {max_sum - min_sum}')