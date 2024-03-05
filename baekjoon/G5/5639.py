# https://www.acmicpc.net/status?problem_id=5639&user_id=fprhqkrtk303
# https://velog.io/@main_door/%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC%EC%99%80-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8A%B8%EB%A6%AC
# https://www.acmicpc.net/board/view/90282

"""
50
30
24
5
27
25
26
28
29
45
98
52
60
106
109
108
110 
"""

import sys
input = sys.stdin.readline

nodes = []
while True:
    try:
        nodes.append(int(input().rstrip()))
    except:
        break

N, M = len(nodes), max(nodes)
tree = [0] * (M + 1)
left = [0] * (M + 1)
right = [0] * (M + 1)

"""
    현재 위치를 루트로 설정, 다음 입력값이 루트보다 작으면
    현재 위치를 스택에 넣고, 다음 입력값 현재 위치의 왼쪽 자식으로 설정
    이후 현재 위치를 루트로 설정 후 재귀

    다음 입력값이 현재 위치보다 크다면 현재 위치의 부모->루트 노드까지 크기 비교
    입력값보다 큰 값이 루트보다 작으면 큰 값의 오른쪽 자식으로 입력값 삽입
    이후 루트로 이동?
"""
def postorder(t):
    if t:
        postorder(left[t])
        postorder(right[t])
        print(t)

# 전위 순회 결과값의 첫 번째는 루트
root = nodes[0]
for i in nodes[1:]:
    if i < root:
        tree[i] = root
        left[root] = i
        root = i
    elif i > root:
        while i > tree[root] and tree[root] != 0:
            root = tree[root]
        tree[i] = root
        right[root] = i
        root = i

postorder(nodes[0])
