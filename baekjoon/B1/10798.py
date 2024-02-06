# https://www.acmicpc.net/problem/10798

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

words = [input().rstrip() for _ in range(5)]

max_length = len(words[0])
for i in range(1, 5):
    if max_length < len(words[i]):
        max_length = len(words[i])

for c in range(max_length):
    for r in range(5):
        try:
            print(words[r][c], end='')
        except:
            pass
print()