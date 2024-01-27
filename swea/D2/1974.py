import sys

sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T + 1):
    grid = []
    is_dup = False

    for i in range(9):
        i = list(map(int, input().split()))
        grid.append(i)


    def is_duplicate(input):
        for num in input:
            if input.count(num) == 1:
                continue
            else:
                return True

    # row comparison
    for row in grid:
        if is_duplicate(row):
            is_dup = True
            break

    # column comparison
    if not is_dup:
        for c in range(9):
            column = []
            for r in range(9):
                column.append(grid[r][c])
            if is_duplicate(column):
                is_dup = True
                break

    # small grid comparison
    if not is_dup:
        r_init = 0
        while not is_dup and r_init <= 6:
            c_init = 0
            while not is_dup and c_init <= 6:
                small_grid = []
                for r in range(r_init, r_init+3):
                    for c in range(c_init, c_init+3):
                        small_grid.append(grid[r][c])
                if is_duplicate(small_grid):
                    is_dup = True
                    break
                else:
                    c_init += 3
            r_init += 3 


    if is_dup:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')
