n = int(input())

list = []
for i in range(n):
    num = int(input())
    list.append(num)

for j in sorted(list):
    print(j)