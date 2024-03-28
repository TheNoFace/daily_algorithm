import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0, 0]

visited = [[0] * N for _ in range(N)]
def search(div):
    if div == 0:
        return

    for sr in range(0, N, div):
        for sc in range(0, N, div):
            init = grid[sr][sc]
            visit_stack = []
            count = 0
            if not visited[sr][sc]:
                for r in range(sr, sr + div):
                    for c in range(sc, sc + div):
                        if init == grid[r][c]:
                            visit_stack.append((r, c))
                            count += 1
                            init = grid[r][c]
                        else:
                            search(div // 3)
                            return
                else:
                    for _ in range(len(visit_stack)):
                        r, c = visit_stack.pop()
                        visited[r][c] = 1
                    result[init] += 1
    return

search(N)
for i in range(-1, 2):
    print(result[i])
