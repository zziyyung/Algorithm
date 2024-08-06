# 위에서 아래로

N = int(input())

data = []

for _ in range(N):
    data.append(int(input()))

result = sorted(data, reverse=True)

for i in result:
    print(i,end=' ')