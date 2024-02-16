# https://www.acmicpc.net/status?problem_id=18258&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

N = int(input().rstrip())
front = 0
rear = -1
q = []

for _ in range(N):
    cmd = list(map(str, input().split()))
    command = cmd[0]
    if command == 'push':
        q.append(cmd[1])
        rear += 1
    elif command == 'pop':
        if rear - front >= 0:
            print(q[front])
            front += 1
            if front > rear:
                q.clear()
                front = 0
                rear = -1
        else:
            print(-1)
    elif command == 'size':
        print(rear - front + 1)
    elif command == 'empty':
        if rear - front >= 0:
            print(0)
        else:
            q.clear()
            print(1)
    elif command == 'front':
        if rear - front >= 0:
            print(q[front])
        else:
            print(-1)
    elif command == 'back':
        if rear - front >= 0:
            print(q[rear])
        else:
            print(-1)
