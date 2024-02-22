# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYaQ5vFKXSEDFAVQ&probBoxId=AY3OawRaBR4DFAUZ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    dec = float(input())

    i = 0
    bin_fractional = ''
    dec *= 2
    while True:
        if i > 13:
            bin_fractional = 'overflow'
            break

        if dec > 1:
            bin_fractional += '1'
            dec -= 1
        elif dec < 1:
            bin_fractional += '0'
        else:
            bin_fractional += '1'
            break

        dec *= 2
        i += 1

    print(f'#{t} {bin_fractional}')
