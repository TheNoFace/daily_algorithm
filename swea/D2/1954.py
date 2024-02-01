# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

T = int(input())

snails = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for _ in range(T):
    snails.append(int(input()))

for t in range(1, T+1):
    print(f'#{t}')
    N = snails[t-1]
    snail = [[0] * N for i in range(N)]

    # 현재 방향
    d = 0
    #  현재 위치
    r = c = 0

    # 반복을 위해 r, c 위치에 숫자를 놓고 r, c를 다음 위치로, 숫자 += 1
    for i in range(1, N*N+1):
        snail[r][c] = i

        # 방향 전환 시기
        # 배열의 범위를 벗어났을 때
        # 이전에 놓은 숫자를 만났을 때
        if r + dr[d] < 0 or r + dr[d] >= N or c + dc[d] < 0 or c + dc[d] >= N:
            d = d + 1 if d < 3 else 0
        elif snail[r + dr[d]][c + dc[d]] != 0:
            d = d + 1 if d < 3 else 0

        r += dr[d]
        c += dc[d]

    c = 0
    for r in range(N):
        for c in range(N):
            print(snail[r][c], end=' ')
            c += 1
            if c >= N:
                print()