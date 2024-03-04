#

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")
input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    def preorder(root):
        if root != 0:
            root_idx = ord(root) - 64
            print(root, end='')
            preorder(left[root_idx])
            preorder(right[root_idx])

    def inorder(root):
        if root != 0:
            root_idx = ord(root) - 64
            inorder(left[root_idx])
            print(root, end='')
            inorder(right[root_idx])

    def postorder(root):
        if root != 0:
            root_idx = ord(root) - 64
            postorder(left[root_idx])
            postorder(right[root_idx])
            print(root, end='')

    for i in range(1, N + 1):
        p, l, r = map(str, input().split())
        p_idx = ord(p) - 64
        l_idx = ord(l) - 64
        r_idx = ord(r) - 64

        if l != ".":
            left[p_idx] = l
        if r != ".":
            right[p_idx] = r

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
    print()
