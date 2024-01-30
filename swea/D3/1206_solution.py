import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/1206.txt", "r")
input = sys.stdin.readline

for t in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))

    # 조망권 수
    count = 0

    for i in range(2, N - 2):
        height = B[i]  # i번 건물의 높이
        # i번 건물의 꼭대기부터 시작, 아래로 내려가면서 조망권 확보 검사
        for floor in range(height, -1, -1):
            # 현재 층에서 좌우 검사
            # i-2 ~ i+2번째 건물보다 현재 층수가 높은지 확인
            if floor > B[i-2] and floor > B[i-1] and floor > B[i+1] and floor > B[i+2]:
                count += 1
            else:
                # 주변 건물 높이가 더 높아지면 중단
                break
    
    print(f'#{t} {count}')
