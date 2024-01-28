# https://www.acmicpc.net/problem/1966

import sys
sys.stdin = open("1966.txt", "r")

T = int(input())

for _ in range(T):
    N, Q = list(map(int, input().split()))
    test_case = list(map(int, input().split()))
    query = test_case[Q]

    def index_counter(pos, input_list):
        length = len(input_list)
        if pos > 0:
            pos -= 1
        else:
            pos = length - 1
        return pos


    count = 0
    while len(test_case) > 0:
        # print('BEF', test_case, Q, count)
        while True:
            max_priority = max(test_case)
            if test_case[0] < max_priority:
                # print('POP', test_case, Q, count)
                test_case.append(test_case.pop(0))
                Q = index_counter(Q, test_case)
            else:
                to_pop = test_case[0]
                count += 1
                if to_pop == max_priority:
                    if Q == 0:
                        # print('FND', test_case, Q, count)
                        break
                    else:
                        # print('DLY', test_case, Q, count)
                        test_case.pop(0)
                        Q = index_counter(Q, test_case)
        if to_pop == query:
            if Q == 0:
                break
            else:
                continue
    
    print(count+Q)
