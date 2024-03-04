# https://www.acmicpc.net/status?problem_id=11725&user_id=fprhqkrtk303
# https://www.acmicpc.net/board/view/99171

import sys

input = sys.stdin.readline

N = int(input().rstrip())
parent = [0] * (N + 1)
right = [0] * (N + 1)
left = [0] * (N + 1)

"""
    0) 입력 값을 원소마다 오름차순 정렬 후 전체 오름차순 정렬
    1) parent[입력 값 둘 중 하나] != 0 이라면
       혹은 입력 값 둘 중 하나 == 1 이라면
    2) 위의 값을 부모 인덱스로 하는 왼쪽 자식 배열에 넣음
       왼쪽 자식이 이미 있다면 오른쪽 자식 배열에 넣음
    3) parent[자식 배열에 넣은 번호] = 입력 값
"""
nodes = [sorted(list(map(int, input().split()))) for _ in range(N - 1)]
nodes.sort(key=lambda x: x[0])
for node in nodes:
    n1, n2 = node

    if n1 == 1 or parent[n1] != 0:
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2
        parent[n2] = n1
    elif n2 == 1 or parent[n2] != 0:
        if left[n2] == 0:
            left[n2] = n1
        else:
            right[n2] = n1
        parent[n1] = n2
    else:
        if left[n1] == 0:
            left[n1] = n2
        else:
            right[n1] = n2
        parent[n2] = n1

for i in range(2, N + 1):
    print(parent[i])
