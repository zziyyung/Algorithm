# 백준 11650: 좌표 정렬하기

n = int(input())
data = []

for _ in range(n):
    data.append(tuple(map(int, input().split())))

# 튜플의 기본 정렬 속성으로 그냥 정렬하기만 하면 됨
data.sort()

for i in range(len(data)):
    print(data[i][0],data[i][1],end='\n')