import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    
    def max_min(nums):
        max_v = min_v = nums[0]
        for i in nums:
            if i > max_v:
                max_v = i
            elif i < min_v:
                min_v = i
            else:
                continue
        return max_v - min_v

    nums_sum = []
    for i in range(0, N-M+1):
        temp = 0
        for j in range(i, i+M):
            temp += array[j]
        nums_sum.append(temp)
    
    print(f'#{t} {max_min(nums_sum)}')
