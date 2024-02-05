# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

weirdo = {
    "ZRO": 0, "ONE": 1, "TWO":2, "THR": 3, "FOR": 4,
    "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}

T = int(input())
for t in range(1, T+1):
    N = int(list(map(str, input().split()))[1])
    words = list(map(str, input().split()))

    # 카운팅 정렬 활용
    count = [0] * 10

    for word in words:
        count[weirdo[word]] += 1

    # 누적합
    for i in range(1, 10):
        count[i] = count[i] + count[i-1]

    # 카운팅 정렬
    words_sorted = [0] * N
    for i in range(N-1, -1, -1):
        count[weirdo[words[i]]] -= 1
        words_sorted[count[weirdo[words[i]]]] = words[i]

    print(f'#{t}')
    print(*words_sorted)