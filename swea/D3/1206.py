import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/1206.txt", "r")
input = sys.stdin.readline

for n in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):  # 양 끝의 2개는 건물 X
        # 좌/우로 2개 비교
        # 좌/우마다 2개 값 중 큰 값만 비교
        # direction = [-2, -1, 1, 2]
        
        # left_max_value = max(B[i-2], B[i-1])
        # right_max_value = max(B[i+1], B[i+2])
        left_max_value = max(B[i-2:i])
        right_max_value = max(B[i+1:i+3])

        if B[i] > left_max_value and B[i] > right_max_value:
            if left_max_value - right_max_value > 0:
                result += B[i] - left_max_value
            else:
                result += B[i] - right_max_value

    print(f'#{n} {result}')
