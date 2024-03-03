# https://www.acmicpc.net/status?problem_id=3085&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    N = int(input())
    candies = [list(input()) for _ in range(N)]
    colors = ['C', 'P', 'Z', 'Y']
    max_count = 0


    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < N


    def counter():
        global max_count
        for color in colors:
            for r in range(N):
                count = 1
                for c in range(N-1):
                    if candies[r][c] == color and candies[r][c+1] == color:
                        count += 1
                    
                if count == N:
                    return N
                elif max_count < count:
                    max_count = count

            for c in range(N):
                count = 1
                for r in range(N-1):
                    if candies[r][c] == color and candies[r+1][c] == color:
                        count += 1
                    
                if count == N:
                    return N
                elif max_count < count:
                    max_count = count

    if counter() == N:
        max_count = N
    else:
        for r in range(N):
            for c in range(N):
                for d in [(0, 1), (1, 0)]:
                    nr, nc = r+d[0], c+d[1]
                    if is_valid(nr, nc) and candies[r][c] != candies[nr][nc]:
                        candies[r][c], candies[nr][nc] = candies[nr][nc], candies[r][c]
                        counter()
                        candies[nr][nc], candies[r][c] = candies[r][c], candies[nr][nc]
    

    print(f'#{t} {max_count}')
