# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PrmyKAWEDFAUq

def sequential_sort(arr, N):
    array = arr
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr = sequential_sort(arr, N)
    print(f'#{t}', *arr)
    