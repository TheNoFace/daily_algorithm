# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcrVmZaSb0DFAVa&probBoxId=AY5PUAIqnH0DFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0

    def merge_sort(arr):
        global count
        # 최소 부분집합까지 나눔
        if len(arr) == 1:
            return arr
        
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        if left[-1] > right[-1]:
            count += 1

        return merge(left, right)

    def merge(left, right):
        result = [0] * (len(left) + len(right))
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result[l + r] = left[l]
                l += 1
            else:
                result[l + r] = right[r]
                r += 1

        if l < len(left):
            while l < len(left):
                result[l + r] = left[l]
                l += 1
        elif r < len(right):
            while r < len(right):
                result[l + r] = right[r]
                r += 1
        else:
            print(f'{l}/{len(left)}, {r}/{len(right)}')

        return result

    arr = merge_sort(arr)
    print(f'#{t} {arr[N // 2]} {count}')