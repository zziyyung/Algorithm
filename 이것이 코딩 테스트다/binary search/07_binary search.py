# 고정점 찾기

import sys

N = int(input())
array = list(map(int, input().split()))
start = 0
end = N-1


def binary_search(array, start, end):
    if start > end:
        return '-1'
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return binary_search(array, mid+1, end)
    else:
        return binary_search(array, start, mid-1)


res = binary_search(array, start, end)
print(res)