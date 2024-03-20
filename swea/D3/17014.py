# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYzyVay6v90DFAXz&contestProbId=AYdFHq16uboDFAVa&probBoxId=AY5ZiI-qG38DFARi

import sys
import os
from collections import deque

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def operator(n, option):
    if option == 0:
        return n * 2
    elif option == 1:
        return n - 1
    elif option == 2:
        return n + 1
    elif option == 3:
        return n - 10
 
 
def solver_bfs(n, m):
    q = deque()
    q.append(n)
    visited = {n: 0}
 
    while q:
        n = q.popleft()
        for i in range(4):
            result = operator(n, i)
            if result == m:
                return visited[n] + 1
            if 0 < result <= 1000000 and result not in visited:
                q.append(result)
                if result not in visited:
                    visited[result] = visited[n] + 1
 
 
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    print(f"#{t}", solver_bfs(N, M))
