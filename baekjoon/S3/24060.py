# https://www.acmicpc.net/problem/24060

## Referenced
# https://velog.io/@nembizzang/백준-24060-알고리즘-수업-병합-정렬-1-파이썬

import sys

input = sys.stdin.readline

A, K = map(int, input().split())
arr = list(map(int, input().split()))
result, arr_K = -1, []


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = (len(arr) + 1) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    temp = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            temp.append(left[left_idx])
            arr_K.append(left[left_idx])
            left_idx += 1
        else:
            temp.append(right[right_idx])
            arr_K.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        temp.extend(left[left_idx:])
        arr_K.extend(left[left_idx:])

    elif right_idx < len(right):
        temp.extend(right[right_idx:])
        arr_K.extend(right[right_idx:])

    return temp


merge_sort(arr)
if K - 1 < len(arr_K):
    print(arr_K[K - 1])
else:
    print(-1)
