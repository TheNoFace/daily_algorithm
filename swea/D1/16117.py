import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())

for n in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maximum, minimum = arr[0], arr[0]

    for i in arr[1:]:
        if i > maximum:
            maximum = i
        elif i < minimum:
            minimum = i

    print(f'#{n} {maximum - minimum}')