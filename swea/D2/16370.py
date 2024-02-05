# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYY0cqzKavoDFAVw&probBoxId=AY14AqXqTP4DFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    strings = [''.join(input()) for _ in range(2)]
    string1 = set(strings[0])

    char_dict = {}
    for char in string1:
        char_dict[char] = 0

    for char in strings[1]:
        if char in char_dict:
            char_dict[char] += 1
    
    # 딕셔너리 정렬
    # char_dict = sorted(char_dict, key=lambda x: -(char_dict[x]))
    max_value = 0
    for value in char_dict.values():
        if max_value < value:
            max_value = value
    print(f'#{t} {max_value}')