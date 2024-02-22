# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYaQ5ZVKXP8DFAVQ&probBoxId=AY3OawRaBR4DFAUZ

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    N, hex_input = input().split()
    result = []
    
    for i in hex_input:
        hex_to_bin = ''
        dec = int(i, 16)
        for j in range(4):
            hex_to_bin = hex_to_bin + '1' if dec & (1 << j) else hex_to_bin + '0'    
        result.append(''.join(reversed(hex_to_bin)))

    print(f'#{t} {"".join(result)}')
