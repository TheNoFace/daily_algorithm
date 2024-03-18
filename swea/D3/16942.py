# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYcrUx-aSSMDFAVa&probBoxId=AY5PUAIqnH0DFARi

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    def quick_sort(arr, l, r):
        if l < r:
            # pivot 위치 설정
            p = partitioning(arr, l, r)
            # 왼쪽 정렬
            quick_sort(arr, l, p - 1)
            # 오른쪽 정렬
            quick_sort(arr, p + 1, r)
        else:
            return

    def partitioning(arr, l, r):
        # 왼쪽 끝, 오른쪽 끝, 중간 값을 비교하여 중간값을 pivot 설정
        mid = (l + r) // 2

        # 중간값이 왼쪽, 오른쪽값 사이에 있는 경우
        if arr[l] <= arr[mid] and arr[mid] <= arr[r]:
            # 중간값을 pivot으로 설정
            pivot = mid
        # 왼쪽값이 중간값, 오른쪽값 사이에 있는 경우
        elif arr[mid] <= arr[l] and arr[l] <= arr[r]:
            # 왼쪽값을 pivot으로 설정
            pivot = l
        # 오른쪽값이 왼쪽값, 중간값 사이에 있는 경우
        else:
            # 오른쪽값을 pivot으로 설정
            pivot = r

        # pivot을 배열 앞으로 보냄
        arr[pivot], arr[l] = arr[l], arr[pivot]

        # 좌, 우 인덱스 비교용 변수 i, j
        i, j = l, r

        # 좌우 인덱스가 교차할 때까지 반복
        while i <= j:
            while i <= j and arr[i] <= arr[l]:
                i += 1
            while i <= j and arr[j] >= arr[l]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # while 반복 종료, pivot 위치 확정
        arr[l], arr[j] = arr[j], arr[l]
        return j

    quick_sort(arr, 0, N - 1)
    print(f'#{t} {arr[N // 2]}')
