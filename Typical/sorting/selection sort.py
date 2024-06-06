# 선택 정렬 : 반복 1회 당 가장 작은 값을 찾아 맨 앞과 교환하는 방식

array = [8,4,6,2,9,1,3,7,5]

n = len(array)

# 인덱스로 최소값 구함

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    print(array)

# for문 설명
# i = 정렬된 부분의 끝을 의미.
    # n까지인 이유 : 배열의 모든 요소를 한 번씩 정렬된 부분의 끝으로 설정하기 위함
# j = i 이후의 모든 요소를 확인
    # n까지인 이유 : 현재 위치 i 이후의 모든 요소를 비교하기 위함 
# 더 작은 값을 찾으면 최소값의 인덱스를 갱신
# 다 돌면 현재 위치와 최솟값의 위치를 교환