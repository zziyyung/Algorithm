# 삽입 정렬 : 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입

array = [8,4,6,2,9,1,3,7,5]
n = len(array)

for i in range(1,n):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]

print(array)