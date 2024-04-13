# https://www.acmicpc.net/problem/6987

## Referenced
# https://www.acmicpc.net/board/view/124317
# https://brorica.tistory.com/206


import sys

input = sys.stdin.readline


def validator(count, win, tie, lose):
    global valid_match

    if count == 15:
        if sum(win) == 0 and sum(tie) == 0 and sum(lose) == 0:
            valid_match = True
        return

    team_a, team_b = matches[count]
    if win[team_a] > 0 and lose[team_b] > 0:
        win[team_a] -= 1
        lose[team_b] -= 1
        validator(count + 1, win, tie, lose)
        win[team_a] += 1
        lose[team_b] += 1

    if not valid_match:
        if tie[team_a] > 0 and tie[team_b] > 0:
            tie[team_a] -= 1
            tie[team_b] -= 1
            validator(count + 1, win, tie, lose)
            tie[team_a] += 1
            tie[team_b] += 1

    if not valid_match:
        if lose[team_a] > 0 and win[team_b] > 0:
            lose[team_a] -= 1
            win[team_b] -= 1
            validator(count + 1, win, tie, lose)
            lose[team_a] += 1
            win[team_b] += 1


# 경기 생성
matches = []
for i in range(6):
    for j in range(i + 1, 6):
        matches.append((i, j))

results = []
for _ in range(4):
    match_result = list(map(int, input().split()))
    valid_match = False

    win, tie, lose = [], [], []
    for i in range(0, 16, 3):
        win.append(match_result[i])
        tie.append(match_result[i + 1])
        lose.append(match_result[i + 2])

    validator(0, win, tie, lose)

    if valid_match:
        results.append(1)
    else:
        results.append(0)

print(*results)
