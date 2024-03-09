# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

N, tr, tc = map(int, input().split())

def z_search(sr, sc, N, count):
    """
        필요 매개변수
        - 탐색 시작 좌표 sr, sc
        - 탐색 범위 N
        - 시작할 번호 count
    """
    G = 2 ** N // 2
    target_reached = False

    # backtracking
    # tr, tc가 현재 검사할 사분면 안에 있다면 재귀 진입
    if sr <= tr <= sr + 2 ** N - 1 and sc <= tc <= sc + 2 ** N - 1:
        for r in range(sr, sr + G + 1, G):
            for c in range(sc, sc + G + 1, G):
                if G > 2:
                    count, target_reached = z_search(r, c, N - 1, count)
                    if target_reached:
                        return count, target_reached
                else:
                    for sub_r in range(r, r + G):
                        for sub_c in range(c, c + G):
                            if sub_r == tr and sub_c == tc:
                                target_reached = True
                                return count, target_reached
                            count += 1
    # tr, tc가 현재 검사할 사분면 안에 없다면 검사할 사분면의 개수만큼 count 증가
    else:
        count += (2 ** N) ** 2
    return count, target_reached

if (tr, tc) == (0, 0):
    print(0)
else:
    print(z_search(0, 0, N, 0)[0])
