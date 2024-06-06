# 버블 정렬 : 인접한 두 수를 비교하여 정렬

# Output : array = [9,8,7,6,5,4,3,2,1]
array = [8,4,6,2,9,1,3,7,5]
# array = [9,8,7,6,5,4,3,2,1]
# Output : array = [1,2,3,4,5,6,7,8,9]

# def bubble_sort(array):

n = len(array)
print(n)

for i in range(n-1): # 전체 배열을 반복하는 횟수
    print(i)
    for j in range(n-i-1): # 이미 정렬된 요소들은 다시 비교할 필요가 없기 때뭉네 n-i-1
        print(j, end="")
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
        print(array)

# 반복 정의
# i, (n-i): 전체 배열을 반복하는 횟수
# j, (n-i-1) : 각 반복에서 비교할 범위를 지정
    # 1번째 반복에서 배열의 끝까지 비교 (n-1)
    # 2번째 반복에서 마지막 요소는 이미 정렬됨. 따라서 그 전까지만 비교 (n-2)
    # 3번째 반복에서 마지막 두 요소는 이미 정렬. 그 전까지만 비교 (n-3) 