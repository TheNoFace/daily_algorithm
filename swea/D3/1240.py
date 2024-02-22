# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15FZuqAL4CFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

decode = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
          '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9'}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    for r in range(N):
        data = list(map(str, input()))
        if '1' in data:
            encrypted = data

    for i in range(M-1, -1, -1):
        if encrypted[i] == '1':
            test = encrypted[i-55:i+1]
            break

    decrypted = ''
    for i in range(0, 56, 7):
        string = test[i:i+7]
        decrypted += decode[''.join(string)]

    code = 0
    for idx, n in enumerate(decrypted):
        if (idx+1) % 2 == 0:
            code += int(n)
        else:
            code += int(n) * 3

    result = 0
    if code % 10 == 0:
        for n in decrypted:
            result += int(n)

    print(f'#{t} {result}')