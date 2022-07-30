# 백준 1026 보물

# B에서 가장 큰 수는 A의 가장 작은 수끼리  곱 !

# 1. 입력값 받기
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# 2. a
answer = 0
a.sort()

for i in range(n):
    x = a[i]
    y = b.pop(b.index(max(b)))

    answer += (x*y)

print(answer)
