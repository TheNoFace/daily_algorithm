# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT

import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.stdin = open(f"{dir_path}/input.txt", "r")


def dec_to_bin(dec):
    if dec == 1:
        return "1"
    elif dec == 0:
        return "0"
    return dec_to_bin(dec // 2) + str(dec % 2)


T = int(input())
for t in range(1, T + 1):
    N, hex_input = map(str, input().split())

    result = ""
    for i in range(int(N)):
        converted = dec_to_bin(int(hex_input[i], 16))
        if len(converted) < 4:
            for j in range(4 - len(converted)):
                converted = "0" + converted
        result += converted

    print(f"#{t}", result)
