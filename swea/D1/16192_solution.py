# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYYQCjXKMeYDFAVw&probBoxId=AY1X4zx6gsoDFAWX

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())


# 버스를 운행하는 함수
def drive(K, N):
    # return 0 : 충전소가 제대로 배치되지 않아서 운행 불가능
    # return > 0 : 충전소가 제대로 배치되었고, 충전한 횟수가 답이 된다.

    last = 0  # 마지막으로 충전했던 위치
    now = K  # 지금 버스 위치 (처음에는 충전한 상태로 간다고 했으니 K만큼 미리 움직여 두었다.)
    count = 0  # 충전한 횟수

    # 버스 운행 해보기
    # while (종점에 도착할 때까지 반복하는 조건):
    #   현재 위치에 충전소가 없다 => 뒤로 한칸 돌아가기(충전소를 발견할 때까지 반복)
    #       이동하기 전 으로 돌아가버리면 길 없음. 반복 바로 종료
    #   현재 위치에 충전소가 있다 => 다음 위치로 최대한 이동, 충전회수 1 증가

    # 종점에 도착할 때까지
    while now < N:
        # 현재 버스 위치에 충전기가 있나 없나 검사
        # 충전기가 만약 현재 위치에 없다면 뒤로 한칸씩 돌아가면서 찾을때까지 뒤로 간다.
        while stop[now] == 0:
            now -= 1  # 한칸씩 뒤로 간다.
            # 뒤로 가다가 점프 전 위치로 돌아와버리면 길이 없다. 운행 불가능
            if now == last:
                # 반복 종료
                return 0  # 운행 불가

        # 여기 코드가 실행되면 충전기가 제대로 설치 되어 있다는 것
        # 마지막 충전 위치를 갱신 , 현재 위치에 충전기가 있다는 의미
        last = now
        # 다음 위치로 이동(최대한 이동, K만큼 이동)
        now += K
        # 충전 횟수 증가
        count += 1

    # 반복문이 잘 종료가 되었다. now >= N 이라는것이고, 그렇다면 제대로 도착 했다는 의미
    # 지금까지 충전한 횟수를 return
    return count


for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K : 한번 충전시 최대 이동 가능 거리(정류장 개수)
    # N : 버스가 가야할 거리(정류장 개수)
    # M : 충전기 개수

    # 충전소 위치
    charge_list = list(map(int, input().split()))

    # 정류장에 충전소가 있나 없나 여부를 나타내는 배열
    stop = [0] * N
    # stop[i] == 1 => i번 정류장에는 충전소가 있다
    # stop[i] == 0 => i번 정류장에는 충전소가 없다

    for x in charge_list:  # x는 충전소가 있는 정류장 번호
        stop[x] = 1

    answer = drive(K, N)
    print(f"#{tc} {answer}")
