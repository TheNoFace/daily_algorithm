from pprint import pprint
import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    color_data = [list(map(int, input().split())) for i in range(N)]
    array = [[0] * 10 for i in range(10)]

    purple = 0
    for data in color_data:
        for r in range(data[0], data[2]+1):
            for c in range(data[1], data[3]+1):
                array[r][c] += data[4]
                if array[r][c] == 3:
                    purple += 1

    print(f'#{t} {purple}')