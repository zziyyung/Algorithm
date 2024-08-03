# def binary_search(arr, x):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
#
# print(binary_search([2, 3, 4, 10, 40], 10))
# print(binary_search([2, 3, 4, 10, 40], 5))

def binary_search(data,x):
    #  오름차순 정렬
    data.sort()

    # 시작, 끝 정하기
    start = 0
    end = len(data) - 1

    while start <= end:
        # 중간값이 변하기 위해서 len(data)//2 가 아닌 start+end//2 !
        mid = (start+end) // 2

        if data[mid] == x :
            return mid
        elif x < data[mid]:
            end = mid-1
        else:
            start = mid + 1
    return -1

print(binary_search([2, 3, 4, 10, 40], 10))
print(binary_search([2, 3, 4, 10, 40], 5))