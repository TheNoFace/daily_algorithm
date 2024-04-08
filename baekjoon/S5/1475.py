# https://www.acmicpc.net/problem/1475

import sys
input = sys.stdin.readline

N = input().rstrip()
numbers = [0] * 10
count = 0

for i in N:
    if i == '9' or i == '6':
        if numbers[9] > numbers[6]:
            numbers[6] += 1
            count = max(count, numbers[6])
        elif numbers[9] <= numbers[6]:
            numbers[9] += 1
            count = max(count, numbers[9])
    else:
        numbers[int(i)] += 1
        count = max(count, numbers[int(i)])

print(count)