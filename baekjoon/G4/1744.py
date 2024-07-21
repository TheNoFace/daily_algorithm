# https://www.acmicpc.net/problem/1744

## Referenced
# https://codingnotes.tistory.com/170

import sys

input = sys.stdin.readline
N = int(input())
num_pos, num_neg = [], []
result = 0

for _ in range(N):
    num_input = int(input())
    if num_input > 0:
        num_pos.append(num_input)
    else:
        num_neg.append(num_input)

num_pos.sort(reverse=True)  # 양수 배열 내림차순 정렬
num_neg.sort()              # 음수 배열 오름차순 정렬

# 양수 처리
if len(num_pos) % 2 != 0:
    result += num_pos.pop()

for p in range(0, len(num_pos), 2):
    if num_pos[p + 1] == 1:
        result += num_pos[p] + num_pos[p + 1]
    else:
        result += num_pos[p] * num_pos[p + 1]

# 음수 처리
if len(num_neg) % 2 != 0:
    result += num_neg.pop()

for n in range(0, len(num_neg), 2):
    result += num_neg[n] * num_neg[n + 1]

print(result)
