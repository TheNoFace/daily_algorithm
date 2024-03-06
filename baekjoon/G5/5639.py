# https://www.acmicpc.net/status?problem_id=5639&user_id=fprhqkrtk303
# https://velog.io/@main_door/%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%AC%EC%99%80-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-%ED%8A%B8%EB%A6%AC
# https://www.acmicpc.net/board/view/90282

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

nodes = []
while True:
    try:
        nodes.append(int(input().rstrip()))
    except:
        break

M = max(nodes)
left = {}
right = {}

def postorder(t):
    if t:
        postorder(left.get(t, 0))
        postorder(right.get(t, 0))
        print(t)

"""
    루트노드에서부터 차례로 타고 내려가기
"""
# 전위 순회 결과값의 첫 번째는 루트
root = nodes[0]
for i in nodes[1:]:
    while True:
        if i < root:
            if left.get(root, 0) != 0:
                root = left[root]
            else:
                left[root] = i
                root = nodes[0]
                break
        elif i > root:
            if right.get(root, 0) != 0:
                root = right[root]
            else:
                right[root] = i
                root = nodes[0]
                break

postorder(nodes[0])
