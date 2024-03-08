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

    for r in range(sr, sr + G + 1, G):
        for c in range(sc, sc + G + 1, G):
            # 재귀 진입
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
        
    return count, target_reached

print(z_search(0, 0, N, 0)[0])
