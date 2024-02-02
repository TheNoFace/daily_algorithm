import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt")

T = 10
N = 100

for t in range(1, T+1):
    input()  # 필요없는 입력 처리는 저장 X
    ladder = [list(map(int, input().split())) for _ in range(N)]

    # 종료점에서부터 거슬러 올라감
    r = 99
    c = -1

    # 도착지점 찾기
    for i in range(N):
        if ladder[r][i] == 2:
            c = i
    
    # 좌 우 상 순서로 탐색
    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    while r > 0:
        # 현재 위치에서 좌/우를 먼저 확인, 경로가 있으면 좌/우부터 진행
        # 경로가 없으면 위로 진행
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 위치가 유효한지 확인
            if 0 <= nr < N and 0 <= nc < N and ladder[nr][nc] == 1:
                # 유효하면 현재 위치 갱신
                r = nr
                c = nc
                # 지나온 길은 재탐색하지 않도록 0으로 변경
                ladder[r][c] = 0
                break  # 현재 방향이 유효하므로 추가 탐색 X

    print(f'#{t} {c}')