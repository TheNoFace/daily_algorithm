# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcrVmZaSb0DFAVa&probBoxId=AY5PUAIqnH0DFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def merge_sort(l, r):
    global count

    # 최소 부분집합까지 나눔
    if (r - l) == 1:
        return l, r

    mid = (l + r) // 2
    left = merge_sort(l, mid)
    right = merge_sort(mid, r)

    if arr[left[1] - 1] > arr[right[1] - 1]:
        count += 1

    merge(left, right)
    return left[0], right[1]


def merge(left, right):
    length = right[1] - left[0]
    result = [0] * length
    l, r = left[0], right[0]

    idx = 0
    while l < left[1] and r < right[1]:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
            idx += 1
        else:
            result[idx] = arr[r]
            r += 1
            idx += 1

    if l < left[1]:
        while l < left[1]:
            result[idx] = arr[l]
            l += 1
            idx += 1
    elif r < right[1]:
        while r < right[1]:
            result[idx] = arr[r]
            r += 1
            idx += 1

    # 실제 리스트에 복사
    for i in range(length):
        arr[left[0] + i] = result[i]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0

    merge_sort(0, N)
    print(f"#{t} {arr[N // 2]} {count}")
