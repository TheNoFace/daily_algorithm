# https://www.acmicpc.net/problem/2206

## Referenced
# https://www.acmicpc.net/board/view/27386
# https://www.acmicpc.net/board/view/88726
# https://forward-gradually.tistory.com/57

## Cases
# https://www.acmicpc.net/board/view/119335

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(str, input().rstrip())) for _ in range(N)]

def pathfinder(r, c):
    if N == 1 and M == 1:
        return 1

    q = deque()
    q.append((0, r, c))
    visited[0][r][c] = 1
    visited[1][r][c] = 1

    while q:
        broke, sr, sc = q.popleft()
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = sr + d[0], sc + d[1]
            if nr == N - 1 and nc == M - 1:
                return visited[broke][sr][sc] + 1

            if 0 <= nr < N and 0 <= nc < M and not visited[broke][nr][nc]:
                # 진행 가능
                if grid[nr][nc] == "0":
                    q.append((broke, nr, nc))
                    visited[broke][nr][nc] = visited[broke][sr][sc] + 1
                # 진행 불가
                elif grid[nr][nc] == "1":
                    # 이전에 깬 적이 없으면
                    if not broke:
                        # 벽을 부쉈을 경우의 방문배열을 enqueue
                        q.append((1, nr, nc))
                        visited[1][nr][nc] = visited[broke][sr][sc] + 1


# 3차원 방문배열 사용
# https://www.acmicpc.net/board/view/97896
# visited[broke][r][c]: 벽을 부쉈을 경우 broke는 1, 안부쉈을 경우 0 사용
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
result = pathfinder(0, 0)
if result:
    print(result)
else:
    print(-1)
