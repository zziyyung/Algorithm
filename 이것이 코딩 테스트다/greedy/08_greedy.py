# 만들 수 없는 금액

N = int(input())
data = list(map(int,input().split()))

# 데이터 정렬
data.sort()

# 값을 비교할 target 변수 생성 (양의 정수이기 때문에 1로 값 주기)
target = 1

for i in data:
    if target < i:
        break
    target += i

print(target)