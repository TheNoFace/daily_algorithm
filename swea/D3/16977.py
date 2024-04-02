# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcv8A8KK20DFAVa&probBoxId=AY5UrhSaAAIDFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def dfs(N, change, stop, pos):
    """
    N: 정류장 개수
    change: 교환 횟수
    stop: 멈췄던 정류장
    pos: 현재 위치
    """
    global count

    # 종료 조건
    # 1. 현재까지의 교환 횟수가 이전 최소값과 같아질 때
    if change >= count:
        return
    # 2. 현재 배터리로 목적지 도달 가능할 때
    if pos + arr[pos] >= N - 1:
        count = change
        return
    # 3. 남은 배터리로 다음 정류장을 갈 수 없을 때
    if stop:
        while pos < N - 1:
            for i in range(arr[pos], 0, -1):
                pos += 1
                if pos in stop:
                    break
                if pos == N:
                    break
            # for 반복 종료: 목적지 도달 불가
            else:
                return
        # while 반복 종료: 목적지 도달
        count = change
        return

    # 공집합 제외 부분 집합 생성
    subset = N - 2
    for i in range(1 << subset):
        stop = []
        for j in range(subset):
            if i & (1 << j):
                stop.append(j + 2)
        n = len(stop)
        if n > 0:
            # 공집합 제외 정류장 선택 완료, 재귀 진입
            dfs(N, len(stop), stop, pos)


def pathfinder(pos, change, battery):
    """
    pos: 현재 위치
    change: 교환 횟수
    battery: 남은 배터리
    """
    global count

    # 종료 조건
    # 1. 배터리 소진
    if battery < 0:
        return

    # 2. 목적지 도착
    if pos == N:
        if count > change:
            count = change
        return

    # 3. 이전 정차 횟수보다 많음
    if change >= count:
        return

    # 남은 배터리로 목적지 도달 가능하면 종료
    if pos + battery >= N:
        if count > change:
            count = change
        return
    # 불가능하면 재귀 진입
    else:
        # 현재 정류장에서 교환
        pathfinder(pos + 1, change + 1, batteries[pos] - 1)
        # 현재 정류장에서 미교환
        pathfinder(pos + 1, change, battery - 1)


T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0] - 1
    batteries = arr[1:]
    count = N

    # dfs(N, 0, [], 1)
    pathfinder(1, 0, batteries[0] - 1)
    print(f"#{t} {count}")
