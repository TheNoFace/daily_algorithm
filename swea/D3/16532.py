# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYZSmrHqa38DFAVw&probBoxId=AY2geIZ6R-gDFAXh

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
# input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for t in range(1, T + 1):
    # DFS와 방향탐색 조합
    # 미로 == 인접리스트
    N = int(input())
    maze = [list(int(n) for n in (input())) for _ in range(N)]
    result = 0

    # 출발점 찾기
    for idx, row in enumerate(maze):
        try:
            r, c = idx, row.index(2)
            break
        except:
            continue

    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    stack = []
    nr, nc = r, c

    # 이전에 방문한 적이 없고 상하좌우가 벽이 아닌 경우에 자식 노드로 진행
    while True:
        if result == 1:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 미로 범위 내, 벽으로 안막혀있고 이전에 방문한 적이 없으면
            if (0 <= nr < N and 0 <= nc < N) and maze[nr][nc] != 1 and visited[nr][nc] != 1:
                # 방문 기록
                visited[nr][nc] = 1
                # 이전 출발 위치 저장
                stack.append((r, c))
                # 검사 위치 초기화
                r, c = nr, nc
                # 다음 위치가 미로 끝이라면
                if maze[r][c] == 3:
                    result = 1
                break
            # 벽으로 막혀있거나 이전에 방문했다면 다음 방향 탐색
        # break 없이 코드 종료 == 더 이상 진행 불가
        # 이전 출발 위치로 되돌아감
        else:
            # 스택이 비어있으면 탐색 가능 경로 없음; while 반복 종료
            if not stack:
                break
            r, c = stack.pop()
    print(f'#{t} {result}')
