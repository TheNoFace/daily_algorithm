# https://www.acmicpc.net/problem/14550

import sys

input = sys.stdin.readline


while True:
    input_str = list(map(int, input().split()))
    if len(input_str) == 1 and input_str[0] == 0:
        break

    N, S, T = map(int, input_str)
    board = [99999]  # 시작점 설정
    dp = [[-10000 * N] * (N + 1) for _ in range(T + 1)]

    while len(board) != N + 1:
        board.extend(list(map(int, input().split())))

    board.append(99999)  # 종료점 설정
    result = set()

    # 초기값 설정
    for i in range(1, S + 1):
        dp[1][i] = board[i]

    # 직전 턴에 도달한 각 인덱스마다 1 ~ S 눈금의 주사위를 굴림
    for t in range(2, T + 1):
        for idx in range(t - 1, (t - 1) * S + 1):
            for s in range(1, S + 1):
                if idx > N:
                    continue

                # 별 도달
                if idx + s > N:
                    result.add(dp[t - 1][idx])
                else:
                    dp[t][idx + s] = max(dp[t - 1][idx] + board[idx + s], dp[t][idx + s])

    print(max(result))
