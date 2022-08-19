# 파이썬 정렬 라이브러리

# sorted
array = [7,5,9,0,3,1,6,2,4,8]
result = sorted(array)
print(result)

# sort : 별도의 정렬된 리스트가 반환되지 않고 원소 바로 정렬
array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)

# key 매개변수 활용
array = [('바나나',2),('사과',5),('토마토',1)]

def setting(data):
    return data[1]

result = sorted(array,key=setting)
print(result)