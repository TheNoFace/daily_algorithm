# https://www.acmicpc.net/problem/20920

import sys
import os
from pprint import pprint as print

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

word_list = {}
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

# 정렬 기준
# 1. 단어 빈도수
# 2. 해당 단어의 길이
# 3. 알파벳 사전 순        
word_list = sorted(word_list, key=lambda x: (-(word_list[x]), -len(x), x))

[print(i) for i in word_list]
