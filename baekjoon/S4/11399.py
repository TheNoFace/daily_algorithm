# https://www.acmicpc.net/problem/11399

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

for i in range(1, N):
    arr[i] = arr[i-1] + arr[i]

print(sum(arr))