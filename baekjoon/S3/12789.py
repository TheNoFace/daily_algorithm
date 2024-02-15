# https://www.acmicpc.net/status?problem_id=12789&user_id=fprhqkrtk303

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f'{dir_path}/input.txt', 'r')
input = sys.stdin.readline

T = 6
for t in range(1, T+1):
    N = int(input().rstrip())
    order = list(map(int, input().split()))

    min_value = 1
    stack = []
    top = -1

    # 첫 번호를 스택에 넣고 내림차순이면:
    # 스택 top보다 1만큼 작으면 내림차순 끝날 때까지 스택에 push
    # 내림차순 push가 끝났는데, 다음 순서가 min_value가 아니면 sad
    # 스택의 처음이 min_value라면 스택 삭제 후 min_value++
    for i in order:
        # 남은 순서의 처음이 최소값이면 다음 순서로 이동
        if i == min_value:
            print(i, end=' ')
            min_value += 1
        # 최소값이 아니라면
        else:
            # 스택이 비어있으면 현재 순서 push
            if not stack:
                stack.append(i)
                top += 1
            # 스택이 비어있지 않으면
            else:
                # 내림차순이면 push
                if i == stack[top] - 1:
                    stack.append(i)
                    top += 1
                # 내림차순이 아니라면 stack[top]과 min_value 비교 후 스택 비우기
                elif stack[top] == min_value:
                    min_value = stack[0] + 1
                    # stack.clear()
                    while top > -1:
                        print(stack.pop(top), end=' ')
                        top -= 1
                    if i != min_value:
                        stack.append(i)
                        top = 0
                    else:
                        top = -1
                        print(i, end=' ')
                        min_value += 1
                else:
                    print('Sad')
                    break
    else:
        print(*stack[::-1])
        print('Nice')
