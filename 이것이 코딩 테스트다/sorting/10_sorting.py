# 국영수

N = int(input())

data = []
for _ in range(N):
    data.append(input().split())

data.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

for i in data:
    print(i[0])