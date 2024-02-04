# https://www.acmicpc.net/problem/3986

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/3986.txt", "r")
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

good = 0
for word in words:
    if len(word) % 2 != 0:
        continue
    elif len(word) == 2 and word[0] != word[1]:
        continue

    # 스택 사용
    # 스택에 있는 글자가 넣을 글자와 같으면 pop
    # 스택에 있는 글자가 넣을 글자와 다르면 append
    stack = []
    for char in word:
        if stack:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    if len(stack) == 0:
        good += 1

print(good)