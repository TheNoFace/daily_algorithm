# https://www.acmicpc.net/status?problem_id=3085&user_id=fprhqkrtk303
# https://www.acmicpc.net/board/view/58247

import sys
input = sys.stdin.readline

N = int(input())
candies = [list(input().rstrip()) for _ in range(N)]
max_count = 1


def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N


def counter(sr, sc, swap, grid):
    global max_count

    """
        교환된 열 두 개와 교환된 행 하나 확인
        검사 시 연속된 색의 개수 == N이라면 return
    """
    if swap == 2:
        sr, sc = sc, sr  # 행렬 교환
        grid = list(zip(*grid))

    # 행 검사
    count_list = []
    for r in range(sr, sr + 1):
        count = 1
        for c in range(N - 1):
            if grid[r][c] == grid[r][c+1]:
                count += 1
                if count == N:
                    max_count = N
                    return N
            else:
                count_list.append(count)
                count = 1
        count_max = max(count_list)
        if count_max > 1:
            if max_count < count_max:
                max_count = count_max

    # 열 검사
    count_list = []
    for c in range(sc, sc + 2):
        count = 1
        for r in range(0, N - 1):
            if grid[r][c] == grid[r+1][c]:
                count += 1
                if count == N:
                    max_count = N
                    return N
            else:
                count_list.append(count)
                count = 1
        count_max = max(count_list)
        if count_max > 1:
            if max_count < count_max:
                max_count = count_max

def search():
    for r in range(N):
        for c in range(N):
            for d in [(0, 1), (1, 0)]:
                if d == (0, 1): # 오른쪽 교환
                    swap = 1
                else: # 아래쪽 교환
                    swap = 2
                nr, nc = r + d[0], c + d[1]
                if is_valid(nr, nc):
                    candies[r][c], candies[nr][nc] = candies[nr][nc], candies[r][c]
                    if counter(r, c, swap, candies) == N:
                        return
                    candies[nr][nc], candies[r][c] = candies[r][c], candies[nr][nc]

search()
print(max_count)
