# 성적이 낮은 순서로 학생 출력하기

N = int(input())

data = []
# 튜플로 값 넣기
for _ in range(N):
    data.append(tuple(input().split()))

def setiing(value):
    return value[1]

result = sorted(data,key=setiing)

for i in result:
    print(i[0],end=' ')


# 책 답안
N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0],int(input_data[1])))

array = sorted(array,key= lambda student: student[1])

for student in array:
    print(student[0],end=' ')