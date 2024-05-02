# https://www.acmicpc.net/problem/4949

import sys

input = sys.stdin.readline

sentences = []
while True:
    text_input = input().rstrip()
    if text_input == ".":
        break
    else:
        sentences.append(text_input)

for sentence in sentences:
    stack = []
    for char in sentence:
        if char == "[" or char == "(":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break

        if char == ".":
            if not stack:
                print("yes")
            else:
                print("no")
