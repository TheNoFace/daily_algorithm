# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_65wkqsb4DFAWS

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    word, shortcut = input().split()
    # result = len(word) - (word.count(shortcut) * (len(shortcut) - 1))

    # without count()
    def count_shortcut(pattern, text):
        p_index = 0
        t_index = 0
        p_length = len(pattern)
        t_length = len(text)
        count = 0

        while p_index < p_length and t_index < t_length:
            # 패턴과 불일치하면 비교 횟수만큼 텍스트 인덱스 이동
            if pattern[p_index] != text[t_index]:
                t_index = t_index - p_index
                p_index = -1
            t_index += 1
            p_index += 1

            if p_index == p_length:
                count += 1
                p_index = 0

        return count

    result = len(word) - (count_shortcut(shortcut, word) * (len(shortcut) - 1))
    print(f'#{t} {result}')