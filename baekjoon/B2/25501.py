# https://www.acmicpc.net/problem/25501

import sys

input = sys.stdin.readline


def recursion(string, l, r, depth):
    if l >= r:
        return 1, depth
    elif string[l] != string[r]:
        return 0, depth
    else:
        return recursion(string, l + 1, r - 1, depth + 1)


def is_palindrome(string):
    return recursion(string, 0, len(string) - 1, 1)


T = int(input())
for _ in range(T):
    string = input().rstrip()

    result = is_palindrome(string)
    print(result[0], result[1])
