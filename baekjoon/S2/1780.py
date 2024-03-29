import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0]


def search(sr, sc, div):
    global result

    if div == 0:
        return

    init = grid[sr][sc]
    count = 0
    for r in range(sr, sr + div):
        for c in range(sc, sc + div):
            if init == grid[r][c]:
                count += 1
            else:
                break
    # 다 세본 다음 개수가 div가 아니면 재귀 진입
    if count != div**2:
        for r in range(sr, sr + div, div // 3):
            for c in range(sc, sc + div, div // 3):
                search(r, c, div // 3)
    else:
        result[init] += 1
    return


search(0, 0, N)
for i in range(-1, 2):
    print(result[i])
