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

    # 시작 글자의 시작 인덱스와 종료 인덱스 도출
    # 다음 글자의 시작 인덱스와 종료 인덱스 도출
    # 시작 글자의 범위 안에 다음 글자의 범위가 있으면 좋은 단어
    first_char = word[0]
    second_char = 'A' if first_char == 'B' else 'B'
    char_index = {'A': [], 'B': []}

    for idx, char in enumerate(word):
        char_index[char].append(idx)

    # 단어 길이는 짝수이므로 비교 가능한 범위는 1/2
    for i in range(0, len(char_index[first_char]), 2):
        start, end = char_index[first_char][i], char_index[first_char][i+1]
        # 첫 글자의 시작과 종료 사이에 있는 비교할 글자의
        # 시작, 종료 인덱스의 개수가 홀수개면 break
        # 짝수개면 진행
        count = 0
        for value in char_index[second_char]:
            if start < value < end:
                count += 1

        if count % 2 != 0:
            break
        else:
            good += 1
            break

print(good)