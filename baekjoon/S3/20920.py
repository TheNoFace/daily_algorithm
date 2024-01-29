# https://www.acmicpc.net/problem/20920

import sys
import os
# from pprint import pprint as print

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")

input = sys.stdin.readline

N, M = map(int, input().split())

word_list = []
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        word_list.append(word)

word_list.sort()
word_dicts = []
for word in word_list:
    word_dict = {}
    word_dict['word'] = word
    word_dict['length'] = len(word)
    word_dict['count'] = word_list.count(word)
    word_dicts.append(word_dict)

word_dicts = sorted(word_dicts, key = lambda x: x['length'], reverse=True)
word_dicts = sorted(word_dicts, key = lambda x: x['count'], reverse=True)

word_list = []
for word in word_dicts:
    if word['word'] not in word_list:
        word_list.append(word['word'])

[print(i) for i in word_list]
